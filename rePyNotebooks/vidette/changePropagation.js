// use these commands to install and activate:  
// jupyter nbextension install notebooks/vidette/changePropagation.js --user
// jupyter nbextension enable changePropagation --user


define('changePropagation', 
[
    'base/js/namespace'
], function(
    Jupyter
) {
    function change_propagation() {
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
        load_ipython_extension: change_propagation,
        invoke_change_propagation: change_propagation
    };
});