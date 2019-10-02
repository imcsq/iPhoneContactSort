iphone-contact-sort.py
=========

为iPhone通讯录中文名规范姓名（默认第一个字为姓，其余为名）并加入姓名拼音排序，适用于英文界面的中文通讯录条目排序

输入原始.vcf格式通讯录文件，该文件可从iCloud导出，运行程序后输出格式化后的.vcf，随后导回iCloud即可。

Example:

    from iPhoneContactSort import iPhoneContactSort
    
    test = iPhoneContactSort('test.vcf')
    test.Convert()

转换成功后，使用iCloud导入新的通讯录文件即可

Current Runtime: Python 2