var KanbanAPIView = Backbone.View.extend({
    model: app.KanbanBoard,
    el: $('#form-div'),
    template: _.template("Hello world"),
    initialize: function () {
        this.render();
    },

    //'render' provides the logic required to construct the view
    render: function () {

        //'$el' is cached object that push the content defined within it and
        //display the value of 'name' when 'template' access the data
        this.$el.html(template({}));
        return this;
    },
    events: {
        'click #submit-form': 'saveData'
    },
    saveData: function () {
        console.log('see');
        alert('data is entered');
    }
});