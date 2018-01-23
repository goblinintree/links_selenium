# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import os
from PIL import Image


def capture(driver, filename, window_height=800):
    """chrome截屏 
    driver 传进来的驱动
    window_height- 窗口高
    filename-生成截图的文件名 
    """  
    try:
        # driver = webdriver.Chrome() 
        # driver.get(base_url)
        js_get_page_width = "return document.body.scrollWidth"
        js_get_page_height = "return document.body.scrollHeight"
        js_get_page_width_result = driver.execute_script(js_get_page_width)
        js_get_page_height_result = driver.execute_script(js_get_page_height)

        print js_get_page_width_result
        print js_get_page_height_result

        window_width=js_get_page_width_result + 100
        # window_height=800

        count_many = (js_get_page_height_result / window_height) +1
        print count_many
        driver.set_window_size(window_width, window_height)

        img_list = []
        i = 1
        while i <= count_many:
            #先截个首屏
            driver.save_screenshot('Screenshots/wap-'+filename + str(i)+'.png')
            img_list.append('Screenshots/wap-'+filename + str(i)+'.png')
            time.sleep(2)
            #滚屏
            js_scroll_screen="window.scrollBy(0, "+str(window_height)+");"
            print js_scroll_screen
            driver.execute_script(js_scroll_screen)
            #准备下次截屏
            i=i+1

        print u"准备合并分屏图"
        image_merge(img_list, "Screenshots", filename+'.png')
    except Exception,e:
        print e


def capture_lazy(driver, filename, window_height=800):
    """chrome截屏 
    driver 传进来的驱动
    window_height- 窗口高
    filename-生成截图的文件名 
    """  
    try:
        # driver = webdriver.Chrome() 
        # driver.get(base_url)
        js_get_page_width = "return document.body.scrollWidth"
        js_get_page_height = "return document.body.scrollHeight"
        js_get_page_width_result = driver.execute_script(js_get_page_width)
        js_get_page_height_result = driver.execute_script(js_get_page_height)

        print js_get_page_width_result
        print js_get_page_height_result

        window_width=js_get_page_width_result + 100
        # window_height=800

        count_many = (js_get_page_height_result / window_height) +1
        print count_many
        driver.set_window_size(window_width, window_height)

        img_list = []
        pos=0
        #先截个首屏
        driver.save_screenshot('Screenshots/wap-'+filename + str(pos)+'.png')
        img_list.append('Screenshots/wap-'+filename + str(pos)+'.png')
        while pos + window_height  < js_get_page_height_result:
            # 页面有未显示出来的部分
            #滚动一屏
            js_scroll_screen="window.scrollBy(0, "+str(window_height)+");"
            print js_scroll_screen
            driver.execute_script(js_scroll_screen)
            #截下滚屏
            driver.save_screenshot('Screenshots/wap-'+filename + str(pos)+'.png')
            img_list.append('Screenshots/wap-'+filename + str(pos)+'.png')
            time.sleep(2)
            #准备下次截屏
            js_get_page_height_result = driver.execute_script(js_get_page_height)
            pos = pos + window_height
            print js_get_page_height_result
            print pos


        print u"准备合并分屏图"
        image_merge(img_list, "Screenshots", filename+'.png')
    except Exception,e:
        print e




def image_merge(images, output_dir, output_name='merge.png', restriction_max_width=None, restriction_max_height=None):  
    """垂直合并多张图片 
    images - 要合并的图片路径列表 
    ouput_dir - 输出路径 
    output_name - 输出文件名 
    restriction_max_width - 限制合并后的图片最大宽度，如果超过将等比缩小 
    restriction_max_height - 限制合并后的图片最大高度，如果超过将等比缩小 
    """  
    def image_resize(img, size=(1500, 1100)):  
        """调整图片大小 
        """  
        print "image_resize"
        try:  
            if img.mode not in ('L', 'RGB'):  
                img = img.convert('RGB')  
            img = img.resize(size)  
        except Exception, e:  
            pass  
        return img 

    print 1
    max_width = 0  
    total_height = 0  
    # 计算合成后图片的宽度（以最宽的为准）和高度  
    for img_path in images:  
        if os.path.exists(img_path):  
            img = Image.open(img_path)  
            width, height = img.size  
            if width > max_width:  
                max_width = width  
            total_height += height  
  
    print 2
    # 产生一张空白图  
    new_img = Image.new('RGB', (max_width, total_height), 255)  
    # 合并  
    x = y = 0  
    for img_path in images:  
        if os.path.exists(img_path):  
            img = Image.open(img_path)  
            width, height = img.size  
            new_img.paste(img, (x, y))  
            y += height  
    print 3
    if restriction_max_width and max_width >= restriction_max_width:  
        # 如果宽带超过限制  
        # 等比例缩小  
        ratio = restriction_max_height / float(max_width)  
        max_width = restriction_max_width  
        total_height = int(total_height * ratio)  
        new_img = image_resize(new_img, size=(max_width, total_height))  
  
    print 4
    if restriction_max_height and total_height >= restriction_max_height:  
        # 如果高度超过限制  
        # 等比例缩小  
        ratio = restriction_max_height / float(total_height)  
        max_width = int(max_width * ratio)  
        total_height = restriction_max_height  
        new_img = image_resize(new_img, size=(max_width, total_height))  

    print 5
    if not os.path.exists(output_dir):  
        os.makedirs(output_dir)
    print 6
    save_path = os.path.join(output_dir, output_name)
    print 7
    print save_path
    # save_path = '%s/%s' % (output_dir, output_name)  
    new_img.save(output_name)  
    # for img_path in images:  
    #     os.remove(img_path)
    return save_path


if __name__ == "__main__":
    driver = webdriver.Chrome() 
    driver.get("http://cn.made-in-china.com/")
    capture(driver, "ABCD",800)