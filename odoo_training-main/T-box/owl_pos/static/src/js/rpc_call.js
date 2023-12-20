odoo.define("owl_pos.call_button", function (require) {
  "use strict";

  var rpc = require("web.rpc");
  var ListController = require("web.ListController");

  ListController.include({
    events: _.extend({}, ListController.prototype.events, {
      "click .call_custom": "get_call_window",
    }),
    get_call_window: function (e) {
      var self = this;
      this._rpc({
        model: "pos.order",
        method: "get_alert_call",
        args: [[]],
      }).then(function (result) {
        window.alert(result);
      });
    },
  });
});
