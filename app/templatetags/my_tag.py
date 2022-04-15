from django import template

# 注册
register = template.Library()


@register.inclusion_tag('my_tag/headers.html')
def banner(menu_name):
    print(menu_name)
    img_list = [
        "http://www.fengfengzhidao.com/media/site_bg/31.jpg",
        "http://www.fengfengzhidao.com/media/site_bg/29.jpg",
        "http://www.fengfengzhidao.com/media/site_bg/28.jpg",
        "http://www.fengfengzhidao.com/media/site_bg/29.jpg",
    ]
    return {'img_list': img_list}
