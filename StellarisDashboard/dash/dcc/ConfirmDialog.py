# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ConfirmDialog(Component):
    """A ConfirmDialog component.
    ConfirmDialog is used to display the browser's native "confirm" modal,
    with an optional message and two buttons ("OK" and "Cancel").
    This ConfirmDialog can be used in conjunction with buttons when the user
    is performing an action that should require an extra step of verification.

    Keyword arguments:

    - id (string; optional):
        The ID of this component, used to identify dash components in
        callbacks. The ID needs to be unique across all of the components
        in an app.

    - cancel_n_clicks (number; default 0):
        Number of times the popup was canceled.

    - cancel_n_clicks_timestamp (number; default -1):
        Last time the cancel button was clicked.

    - displayed (boolean; optional):
        Set to True to send the ConfirmDialog.

    - message (string; optional):
        Message to show in the popup.

    - submit_n_clicks (number; default 0):
        Number of times the submit button was clicked.

    - submit_n_clicks_timestamp (number; default -1):
        Last time the submit button was clicked."""

    _children_props = []
    _base_nodes = ["children"]
    _namespace = "dash_core_components"
    _type = "ConfirmDialog"

    @_explicitize_args
    def __init__(
        self,
        id=Component.UNDEFINED,
        message=Component.UNDEFINED,
        submit_n_clicks=Component.UNDEFINED,
        submit_n_clicks_timestamp=Component.UNDEFINED,
        cancel_n_clicks=Component.UNDEFINED,
        cancel_n_clicks_timestamp=Component.UNDEFINED,
        displayed=Component.UNDEFINED,
        **kwargs
    ):
        self._prop_names = [
            "id",
            "cancel_n_clicks",
            "cancel_n_clicks_timestamp",
            "displayed",
            "message",
            "submit_n_clicks",
            "submit_n_clicks_timestamp",
        ]
        self._valid_wildcard_attributes = []
        self.available_properties = [
            "id",
            "cancel_n_clicks",
            "cancel_n_clicks_timestamp",
            "displayed",
            "message",
            "submit_n_clicks",
            "submit_n_clicks_timestamp",
        ]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ConfirmDialog, self).__init__(**args)
