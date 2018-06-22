import ipywidgets as widgets
class HighCharts(widgets.DOMWidget):
    from traitlets import Dict, Unicode
    _view_name = Unicode('MapboxGLView').tag(sync=True)
    _view_module = Unicode('mapboxglModule').tag(sync=True)
    _view_module_version = Unicode('0.1.0').tag(sync=True)
    value = Dict({"my_key": "Hello"}).tag(sync=True)
    def initialize(self):
        import uuid
        self.this_id = str(uuid.uuid4())
    def writeJsontoEnvironment(self):
        print('adding a variable to the env')
        
    
    def plot(self, variable_name, *args, **kwargs):
        from IPython.core.display import Javascript
#         import json
#         json_config = json.dumps(chart)
        this_id = self.this_id
        return Javascript("""
            require.undef('mapboxglModule');
            require.config({
              paths: {
                highcharts: "http://code.highcharts.com/highcharts",
                highcharts_exports: "http://code.highcharts.com/modules/exporting",
              },
              shim: {
                highcharts: {
                  exports: "Highcharts",
                  deps: ["jquery"]
                },
                highcharts_exports: {
                  exports: "Highcharts",
                  deps: ["highcharts"]
                }
              }
            });
            
            define('mapboxglModule', ["@jupyter-widgets/base", "highcharts_exports", "changePropagation"], (widgets, highcharts, changePropagation) => {
            
            let MapboxGLView = widgets.DOMWidgetView.extend({
                defaults: _.extend({}, widgets.DOMWidgetModel.prototype.defaults, { value: '' }),
                placeholder_id : null,
                generate_placeholder_id : function() {
                    return Math.random().toString(36).substring(7);
                },
                render: function() {
                    //this.value_changed();
                    console.log('placeholder id:', this.placeholder_id);
                    if (this.placeholder_id === null){
                        this.placeholder_id = this.generate_placeholder_id();
                    }
                    console.log('placeholder id:', this.placeholder_id);
                    
                    if($("#container").length == 0) {
                      this.create_dom_element();
                    }
                    
                    function exec_code(context){
                        var kernel = IPython.notebook.kernel;
                        var code_input = '"""+variable_name+"""';
                        console.log('code input', code_input);

                        var msg_id = kernel.execute(code_input, {
                            iopub: {
                                output: function(response) {
                                    // Print the return value of the Python code to the console
                                    var result = response.content.data["text/plain"].replace(/'/g, '"');;
                                    //console.log(result);
                                    var chart = JSON.parse(result)
                                    console.log('currently obtained chart', chart);
                                    context.display_highcharts(JSON.parse(result));
                                    
                                }
                            }
                        },
                        {
                            silent: false, 
                            store_history: false, 
                            stop_on_error: true
                        });
                    }
                    
                    
                    exec_code(this);
                    //this.model.on('change:value', this.value_changed, this);
                },
                value_changed: function() {
                    this.el.textContent = this.model.get('value').my_key;
                },
                
                callback: function(e) {
                    // function triggered as a result of user selecting a particular region
                    var kernel = IPython.notebook.kernel;
                    var code_input = '"""+variable_name+"""';
                    /*var msg_id = kernel.execute(code_input, {
                            iopub: {
                                output: function(response) {
                                    var result = response.content.data["text/plain"].replace(/'/g, '"');;
                                    var chart = JSON.parse(result)
                                    console.log("printing unchanged config: " + chart.xAxis);
                                    chart.xAxis.max = e.max;
                                    chart.xAxis.min = e.min;
                                    
                                    var kernel = IPython.notebook.kernel;
                                    kernel.execute('chart["xAxis"]["min"] = '+e.min)
                                    kernel.execute('chart["xAxis"]["max"] = '+e.max)
                                    console.log(changePropagation);
                                    console.log(changePropagation.load_ipython_extension())
                                    // changePropagation.load_ipython_extension();
                                    changePropagation.invoke_change_propagation();
                                    // changePropagation.change_propagation();
                                }
                            }
                        },
                        {
                            silent: false, 
                            store_history: false, 
                            stop_on_error: true
                        });
*/
		    var kernel = IPython.notebook.kernel;
		    kernel.execute('minx = '+e.min);
		    kernel.execute('maxx = '+e.max);
		    changePropagation.invoke_change_propagation();
                    
                },
                
                create_dom_element : function() {
                    element.append('<div id=\""""+this_id+"""\" style="min-width: 310px; height: 400px; margin: 0 auto"></div>');
                },
                display_highcharts: function(chart) {
                    // need to check if provided config file contains the following attributes
                    // if it does do not overwrite.
                    if (!chart.hasOwnProperty('xAxis')){
                        chart.xAxis = {};
                    }
                    if (!chart.xAxis.hasOwnProperty('events')){
                        chart.xAxis.events = {};
                    }
                    chart.xAxis.events.setExtremes = this.callback;
                    var kernel = IPython.notebook.kernel;
                    //var code_input = '"""+variable_name+""" = chart';
                    //var msg_id = kernel.execute(code_input, {
                    //        iopub: {
                    //            output: function(response) {
                    //                // Print the return value of the Python code to the console
                    //                var result = response.content.data["text/plain"].replace(/'/g, '"');;
                    //                var chart = JSON.parse(result)
                    //                //context.display_highcharts(JSON.parse(result));
                    //                
                    //            }
                    //        }
                    //    },
                    //    {
                    //        silent: false, 
                    //        store_history: false, 
                    //        stop_on_error: true
                    //    });
                    var this_id = '"""+this_id+"""';
                    console.log('this id', this_id);
                    console.log('about to display chart:',chart);
                    var attached_chart = $('#'+this_id).highcharts(chart);
                    console.log('attached_chart', attached_chart);
                    
                },
                });
            return {
                    MapboxGLView,
                };
            });
        """)
