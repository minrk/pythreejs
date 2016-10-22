//
// This file auto-generated with generate-wrappers.js
// Date: Fri Oct 21 2016 17:17:08 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var ThreeModel = require('../_base/Three').ThreeModel;
var ThreeView = require('../_base/Three').ThreeView;


var Matrix4Model = ThreeModel.extend({

    defaults: _.extend({}, ThreeModel.prototype.defaults, {

        _view_name: 'Matrix4View',
        _model_name: 'Matrix4Model',

        elements: [],

    }),

    constructThreeObject: function() {

        return new THREE.Matrix4();

    },

    createPropertiesArrays: function() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        

        this.property_converters['elements'] = null;

    },

});

var Matrix4View = ThreeView.extend({});

module.exports = {
    Matrix4View: Matrix4View,
    Matrix4Model: Matrix4Model,
};