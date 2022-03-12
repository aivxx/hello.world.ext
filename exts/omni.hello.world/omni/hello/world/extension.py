import omni.ext
import omni.ui as ui

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.hello.world] MyExtension startup")

        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                with ui.ZStack():
                
                 with ui.Placer(offset_x=1, offset_y=1):
                    
                  ui.Label("Hello World", height=50, style={"font_size":24})
                ui.Button("This is a button", style= {"color":0xFF00AA00})

                ui.Separator(height=5)
                with ui.HStack(height=5):
                    ui.Button("Another Button")
                    ui.Button("A button here")
                    ui.Button("One more")
           

                def on_click():
                    print("clicked!")

                ui.Button("Click Me", clicked_fn=lambda: on_click())

                ui.IntSlider(height=30).model.set_value(10)
                ui.Spacer(height=10)
        
      
               
         

    def on_shutdown(self):
        print("[omni.hello.world] MyExtension shutdown")
