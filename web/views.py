from __future__ import annotations

import re
from typing import Any, List, Tuple

from django.contrib import messages
from django.db import connection, transaction, connections
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import SqlQueryForm


READ_ONLY_PATTERN = re.compile(r"^\s*(SELECT|WITH)\b", re.IGNORECASE | re.DOTALL)
WRITE_PATTERN = re.compile(
    r"\b(INSERT|UPDATE|DELETE|MERGE|EXEC(?:UTE)?|CREATE|ALTER|DROP|TRUNCATE|GRANT|REVOKE|DENY|DBCC|BACKUP|RESTORE|USE|BEGIN|COMMIT|ROLLBACK)\b",
    re.IGNORECASE,
)


def _is_read_only_query(sql: str) -> bool:
    # Must start with SELECT/CTE, contain no semicolons, and no write/admin keywords
    if not READ_ONLY_PATTERN.match(sql):
        return False
    if ";" in sql:
        return False
    if WRITE_PATTERN.search(sql):
        return False
    return True


def index(request: HttpRequest) -> HttpResponse:
    form = SqlQueryForm(request.POST or None)
    columns: List[str] = []
    rows: List[Tuple[Any, ...]] = []

    if request.method == "POST" and form.is_valid():
        sql = form.cleaned_data["sql"].strip().rstrip(";")
        if not _is_read_only_query(sql):
            messages.error(request, "Only SELECT/CTE queries are allowed.")
        else:
            try:
                # Prefer MSSQL connection if configured, else default
                db_alias = "mssql" if "mssql" in connections else "default"
                with connections[db_alias].cursor() as cursor:
                    cursor.execute(sql)
                    description = cursor.description or []
                    columns = [col[0] for col in description]
                    rows = list(cursor.fetchmany(1000))  # limit to 1000 rows for safety
                    if cursor.nextset():
                        messages.info(request, "Note: Only the first result set is shown.")
            except Exception as exc:  # noqa: BLE001
                messages.error(request, f"Error executing query: {exc}")

    context = {"form": form, "columns": columns, "rows": rows}
    return render(request, "web/index.html", context)
