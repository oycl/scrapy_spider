# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AntAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    build_data = scrapy.Field()
    index = scrapy.Field()
    url = scrapy.Field()
    cert_code = scrapy.Field()
    flow_no = scrapy.Field()
    set_date = scrapy.Field()
    print_date = scrapy.Field()
    type = scrapy.Field()
    ip = scrapy.Field()
    bank_name = scrapy.Field()
    department = scrapy.Field()
    other_matter = scrapy.Field()
    information_update_time = scrapy.Field()
    company_name = scrapy.Field()
    platform = scrapy.Field()
    signing_time = scrapy.Field()
    online_time = scrapy.Field()
    credit_code = scrapy.Field()
    system_name = scrapy.Field()
    system_version = scrapy.Field()
    productUrl = scrapy.Field()


class onlineloanItem(scrapy.Item):
    # define the fields for your item here like:
    platform = scrapy.Field()#平台名称
    amount = scrapy.Field()#额度
    term = scrapy.Field()#期限
    interest = scrapy.Field()#利率
    phone = scrapy.Field()#电话
    credit = scrapy.Field()#征信
    actual_amount = scrapy.Field()#实际到账
    sort = scrapy.Field()#类别
    material = scrapy.Field()#资料
    characteristic = scrapy.Field()#特点
    number_people = scrapy.Field()#申请人数
    arrival = scrapy.Field()#到帐方式
    speed = scrapy.Field()#放款速度
    review = scrapy.Field()#审核方式
    other = scrapy.Field()
    name = scrapy.Field()#平台名称
    platformname = scrapy.Field()#平台名称
    expense = scrapy.Field()#费用（利率）
    amount_high = scrapy.Field()#额度高低



class AppItem(scrapy.Item):
    # define the fields for your item here like:
    keyword = scrapy.Field()
    apk_md5 = scrapy.Field()
    apk_public_time = scrapy.Field()
    apk_url = scrapy.Field()
    app_downcount = scrapy.Field()
    app_id = scrapy.Field()
    app_name = scrapy.Field()
    author_name = scrapy.Field()
    description = scrapy.Field()
    pkg_name = scrapy.Field()

class lianjia(scrapy.Item):
    first_name = scrapy.Field()
    second_name = scrapy.Field()
    total_num = scrapy.Field()
    first_num = scrapy.Field()
    second_num = scrapy.Field()
    first_url = scrapy.Field()
    second_url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    price_unit = scrapy.Field()
    price = scrapy.Field()
    cenggao = scrapy.Field()
    chaoxiang = scrapy.Field()
    ceng = scrapy.Field()
    mianji = scrapy.Field()
    jianchengshijian = scrapy.Field()
    xiaoqu = scrapy.Field()
    quyu = scrapy.Field()
    kanfangshijian = scrapy.Field()
    lianjiaid = scrapy.Field()
    huxin = scrapy.Field()
    taoneimianji = scrapy.Field()
    diantibi = scrapy.Field()
    dianti = scrapy.Field()
    chanquan = scrapy.Field()
    guapaishijian = scrapy.Field()
    quanshu = scrapy.Field()
    shangcijiaoyi = scrapy.Field()
    yongtu = scrapy.Field()
    nianxian = scrapy.Field()
    chanquansuoshu = scrapy.Field()
    diyaxinxi = scrapy.Field()
    fanbenbeifeng = scrapy.Field()
    fanxieid = scrapy.Field()
    tag = scrapy.Field()
    tese = scrapy.Field()
    room_information = scrapy.Field()
    ziquyu = scrapy.Field()
    detail_url = scrapy.Field()

class test(scrapy.Item):
    state = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()

class boss(scrapy.Item):
    url = scrapy.Field()
    job_status = scrapy.Field()
    name = scrapy.Field()
    xinzhi = scrapy.Field()
    information = scrapy.Field()
    fuli = scrapy.Field()
    yaoqiu = scrapy.Field()
    gongsijieshao = scrapy.Field()
    gongsi = scrapy.Field()
    chenglishijian = scrapy.Field()
    dizhi = scrapy.Field()
    shangshi = scrapy.Field()
    renshu = scrapy.Field()
    hangye = scrapy.Field()
    zhucezijin = scrapy.Field()

class yamaxun(scrapy.Item):
    name = scrapy.Field()
    information = scrapy.Field()
    phonenum = scrapy.Field()
    fenlei_url = scrapy.Field()
    fenlei_name = scrapy.Field()
    more_url = scrapy.Field()
    shanghu_url = scrapy.Field()
    shanghu_name = scrapy.Field()
    detailurl = scrapy.Field()
    
class flcrm(scrapy.Item):
    company_name = scrapy.Field()
    email = scrapy.Field()
    address = scrapy.Field()
    products = scrapy.Field()
    area = scrapy.Field()
    sourceName = scrapy.Field()
    promoterName = scrapy.Field()
    state = scrapy.Field()
    levelValue = scrapy.Field()
    createTime = scrapy.Field()
    site = scrapy.Field()
    industryName = scrapy.Field()
    jobName = scrapy.Field()
    name = scrapy.Field()
    mobile = scrapy.Field()
    telphone = scrapy.Field()

class softtime(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    NodeId = scrapy.Field()
    name = scrapy.Field()
    SaleCount = scrapy.Field()
    BrandCount = scrapy.Field()
    Url = scrapy.Field()
    Id = scrapy.Field()
    ASIN = scrapy.Field()
    Name = scrapy.Field()
    NameEncode = scrapy.Field()
    Brand = scrapy.Field()
    BrandEncode = scrapy.Field()
    ImageEncode = scrapy.Field()
    Store = scrapy.Field()
    Rank = scrapy.Field()
    Solder = scrapy.Field()
    CommentCount = scrapy.Field()
    SaleTime = scrapy.Field()
    Score = scrapy.Field()
    Variants = scrapy.Field()
    OtherSellerCount = scrapy.Field()
    EBC = scrapy.Field()
    CurrentSalePrice = scrapy.Field()
    SalePrice = scrapy.Field()
    PromotionRecords = scrapy.Field()
    PotentialEvaluation = scrapy.Field()
    Income = scrapy.Field()
    FBAFee = scrapy.Field()
    BestSeller = scrapy.Field()
    ListingHeight = scrapy.Field()
    ListingWidth = scrapy.Field()
    ListingDepath = scrapy.Field()
    SizeStr = scrapy.Field()
    ShippingWeight = scrapy.Field()
    PickAndPack = scrapy.Field()
    Referral = scrapy.Field()
    Storage = scrapy.Field()
    Deliver = scrapy.Field()
    ReferralRate = scrapy.Field()
    TypeName = scrapy.Field()
    Image = scrapy.Field()
    BrandSalePercent = scrapy.Field()
    TotalSalePercent = scrapy.Field()
    BDCount = scrapy.Field()
    Coupon = scrapy.Field()
    CouponRecord = scrapy.Field()
    ActualSalePrice = scrapy.Field()
    Volume = scrapy.Field()
    Productsize = scrapy.Field()
    totalsalecount = scrapy.Field()







