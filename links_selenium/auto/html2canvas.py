# -*- coding: UTF-8 -*-
from selenium import webdriver


def driver_add_element_to_tag(driver, tag, element):

    pass





if __name__ == "__main__":
    driver = webdriver.Chrome() 
    driver.get("http://cn.made-in-china.com/")
    # script_tag_js_src='<script type="text/javascript" src="https://cdn.bootcss.com/html2canvas/0.5.0-beta4/html2canvas.min.js"></script>'
    # js_script_src='''
    #     var script = document.createElement("script");
    #     script.type = "text/javascript";
    #     script.src = "https://cdn.bootcss.com/html2canvas/0.5.0-beta4/html2canvas.min.js";
    #     document.body.appendChild(script);
    #     '''
    js_loadscript_function='''
        function loadscript(url) {
            var script = document.createElement("script");
            script.type = "text/javacript";
            script.src = url;
            document.body.appendChild(script);
        }
        '''
    driver.execute_script(js_loadscript_function)
    js_loadscript_html2canvas='''
        loadscript("http://cdn.bootcss.com/html2canvas/0.5.0-beta4/html2canvas.min.js")
        '''
    driver.execute_script(js_loadscript_html2canvas)
    js_loadscript_jquery='''
        loadscript("https://code.jquery.com/jquery-3.2.1.min.js")
        '''
    driver.execute_script(js_loadscript_jquery)
    js_pageshot_function='''
        function pageshot(){
            html2canvas($("body"),{
                onrendered:function(canvas){
                    dataURL =canvas.toDataURL("image/png");
                    $("body").append(canvas);
                    console.log(dataURL);

                    $('#down_button').attr( 'href' ,  dataURL ) ;
                    $('#down_button').attr( 'download' , 'myjobdeer.png' ) ;
                },
                width:320,
                height:400
            })
        }
        '''




    tag = ""



    driver.execute_script()