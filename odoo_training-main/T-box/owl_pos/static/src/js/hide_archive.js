odoo.define('owl_pos.hide_action_button', function (require) {

  "use strict";

  var session = require('web.session');
  var BasicView = require('web.BasicView');

  BasicView.include({

    init: function(viewInfo, params) {
      var self = this;
      this._super.apply(this, arguments);

      var current_model = self.controllerParams.modelName;
      var restrict_models = ['product.template'];

      if(restrict_models.includes(current_model) && session.uid !== 2) {
        self.controllerParams.archiveEnabled = 'False' in viewInfo.fields;
      }
    },

  });
});