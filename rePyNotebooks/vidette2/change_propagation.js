// use this command to install:  jupyter nbextension install notebooks/vidette/change_propagation.js --user

define('changePropagation', 
[
    'base/js/namespace'
], function(
    Jupyter
) {
    function change_propagation() {
        
        console.log("this is the change propagation algorithm!!");
        console.log(Jupyter.notebook.get_cells().length);
        var cells = Jupyter.notebook.get_cells();
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            var content = cell.get_text();
//                     console.log(i, content);
            if (content.indexOf("%%init") == -1) {
//                         console.log("not ignore!");
//                         console.log(i, content);
                cell.execute();
            }
        }
    }

    return {
        load_ipython_extension: change_propagation
    };
});