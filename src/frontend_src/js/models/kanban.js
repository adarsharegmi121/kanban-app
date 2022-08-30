var app = app || {} ;

app.KanbanBoard = Backbone.Model.extend({
    defaults:{
        'board_name':'',
    },
    setName:function(name){
        this.set("board_name",name);
    },
    getName:function(){
        return this.get("board_name");
    }
});