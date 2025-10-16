from __future__ import annotations

from django import forms


class SqlQueryForm(forms.Form):
    sql = forms.CharField(
        label="SQL",
        widget=forms.Textarea(attrs={"rows": 6, "placeholder": "SELECT TOP (10) * FROM sys.tables"}),
        help_text="Read-only queries only. DDL/DML blocked.",
    )
