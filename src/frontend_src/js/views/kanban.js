var app = app || {};
app.KanbanAPIView = Backbone.View.extend({
    model: app.KanbanBoard,
    el: $('#form-div'),
    template: _.template("<div>Hello world</div>"),
    intialize: function(){
        this.render();
    },
    render: function () {
        this.$el.html(this.template());
    },
    events:{
        'click #submit-form': 'saveData'
    },
    saveData: function(){
        console.log('see');
        alert('data is entered');
    }
});