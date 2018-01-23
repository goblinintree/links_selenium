# -*- coding: UTF-8 -*-
import xlrd
import json

def xls_url_generator(xls_file=u'file\中文版链接-用例.xls', workbook=None, ignores=[u"temp",u"正式版-账号",u"流程业务"]):
    """
    {   
        "moudle":sheet.name,
        "name":sheet.cell(srow,1).value, 
        "url":sheet.cell(srow,2).value
    }
    """
    if workbook:
        workbook = xlrd.open_workbook(xls_file, encoding_override='GB2312')  
    sheets = workbook.sheets()
    for sheet in  sheets:
        srows = sheet.nrows
        scols = sheet.ncols
        # print srows, scols
        # print ">>>" ,be_ignore(sheet.name, ignores)
        if not (be_ignore(sheet.name, ignores)):
            for srow in range(1, srows):
                if scols >= 3 and (sheet.cell(srow,2).value ):
                    # string = json.dumps({"moudle":sheet.name,"name":sheet.cell(srow,1).value.encode("GB2312","ignore"), "url":sheet.cell(srow,2).value})
                    # yield  {"moudle":sheet.name,"name":sheet.cell(srow,1).value.encode("GB2312","ignore"), "url":sheet.cell(srow,2).value}
                    # string = json.dumps({"moudle":sheet.name,"name":sheet.cell(srow,1).value, "url":sheet.cell(srow,2).value})
                    # yield  string
                    try:
                        scol_3_value = sheet.cell(srow,3).value
                        scol_3_value = int(scol_3_value)
                    except (IndexError, ValueError):
                        scol_3_value = 0
                    # print {"moudle":sheet.name,"name":sheet.cell(srow,1).value, "url":sheet.cell(srow,2).value, "member":scol_3_value}           
                    yield  {"moudle":sheet.name,"name":sheet.cell(srow,1).value, "url":sheet.cell(srow,2).value, "member":scol_3_value}
    pass


def xls_yewu_generator(xls_file=u'file\中文版链接-用例.xls', workbook=None, sures=[u"流程业务"]):
    """
    {   
        "moudle":sheet.name,
        "name":sheet.cell(srow,1).value, 
        "yewu":sheet.cell(srow,2).value,
        "member",sheet.cell(srow,3).value
    }
    """
    if workbook:
        workbook = xlrd.open_workbook(xls_file, encoding_override='GB2312')  
    sheets = workbook.sheets()
    for sheet in  sheets:
        srows = sheet.nrows
        scols = sheet.ncols
        # print srows, scols
        # print ">>>" ,be_ignore(sheet.name, ignores)
        if (be_sure(sheet.name, sures)):
            for srow in range(1, srows):
                if scols >= 3 and (sheet.cell(srow,2).value ):
                    try:
                        scol_3_value = sheet.cell(srow,3).value
                        scol_3_value = int(scol_3_value)
                    except (IndexError, ValueError):
                        scol_3_value = 0
                    yield  {"moudle":sheet.name,"name":sheet.cell(srow,1).value, "yewu":sheet.cell(srow,2).value, "member":scol_3_value}
    pass


def be_ignore(sheet, ignores):
    for ignore in ignores :
        if sheet == ignore:
            # print ignore
            return True
    return False


def be_sure(sheet, sures):
    for sure in sures :
        if sheet == sure:
            # print ignore
            return True
    return False


def get_workbook(xls_file=u'file\中文版链接-用例.xls'):
    # print xls_file
    workbook = xlrd.open_workbook(xls_file, encoding_override='GB2312')  
    return workbook


def xls_member_dict(xls_file=u'file\中文版链接-用例.xls',workbook=None, sure=u"正式版-账号", member=30):
    """
    {   
        "member":"30",
        "username":sheet.cell(3,2).value, 
        "password":sheet.cell(3,3).value
    }
    """
    # print xls_file
    if workbook:
        workbook = xlrd.open_workbook(xls_file, encoding_override='GB2312')  
    workbook = xlrd.open_workbook(xls_file, encoding_override='GB2312')  
    sheets = workbook.sheets()
    for sheet in  sheets:
        try:
            srows = sheet.nrows
            scols = sheet.ncols
            # print srows, scols
            if (sheet.name == sure):
                # print sheet.name
                # print type(member)
                # print member
                # print sheet.cell(3,2).value
                # print sheet.cell(3,3).value

                if member == 30:
                    return  {"member":30,"username":sheet.cell(3,2).value, "password":sheet.cell(3,3).value}
                elif member == 25:
                    return  {"member":25,"username":sheet.cell(4,2).value, "password":sheet.cell(4,3).value}
                elif member == 3:
                    return  {"member":3,"username":sheet.cell(5,2).value, "password":sheet.cell(5,3).value}
                elif member == 1:
                    return  {"member":1,"username":sheet.cell(6,2).value, "password":sheet.cell(6,3).value}
                else:
                    return  {"member":30,"username":sheet.cell(3,2).value, "password":sheet.cell(3,3).value}
        except Exception as e:
            print e.message
            return None
            pass
    pass

if __name__ == "__main__":
    #打开Excel文件  
    print "sss"
    xls_file = u'file\中文版链接-用例.xls'
    count = 0
    for string in xls_url_generator(xls_file):
        count = count + 1
        print count 
        print string 
        print "*" * 50