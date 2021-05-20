from RootParsing import *
from Functions import *
import xml.etree.ElementTree as ET
import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="",
                                     database="base_onix")

filname = '324109214'
tree = ET.parse('C:/Users/user/Desktop/basedilicom/{}.xml'.format(filname))
root = tree.getroot()
list_prod = []
list_desc = []
list_cont = []
list_subj = []
list_supp = []
list_pub = []
list_rel = []
list_psupp = []
list_pri = []
#tuple
prod_tuple = ('ISBN', 'GTIN', 'RefInternFournisseur', 'Title', 'Editor', 'Distributor', 'Price', 'TextType',
              'ContentAudience', 'Text', 'BarcodeType', 'PositionOnProduct')
desc_tuple=()
cont_tuple=()
subj_tuple=()
supp_tuple=()
pub_tuple=()
rel_tuple=()
psupp_tuple=()
pri_tuple=()
for pro in root.findall('Product'):
    ##############  Notification condition insert here ##################
    Desc = pro.find('./DescriptiveDetail')
    Coll = pro.find('./CollateralDetail')
    Pub = pro.find('./PublishingDetail')
    Rel = pro.find('./RelatedDetail')
    Psupp = pro.find('./ProductSupply')
    try:
        #################### Product table  ######################
        dict_prod = Product_Parsing(pro)
        list_prod.append(list(dict_prod.values()))
        #################### DescriptiveDetail ###################
        dict_desc = DescDetail_Parsing(pro)
        list_desc.append(list(dict_desc.values()))
        #################### Contributers ####################
        if Desc is not None:
            for cont in Desc.findall('Contributor'):
                dict_cont = Contributor_parsing(pro, cont)
                list_cont.append(list(dict_cont.values()))
            #################### Subjects #####################
            for subj in Desc.findall('Subjects'):
                dict_subj = Subject_parsing(pro, subj)
                list_subj.append(list(dict_subj.values()))
        #################### PublishingDetail #####################
        dict_pub = PublishDetail_parsing(pro)
        list_pub.append(list(dict_pub.values()))
        #################### RelatedMaterial ######################
        dict_rel = RelatedMaterial(pro)
        list_rel.append(list(dict_rel.values()))
        #################### ProductSupply ########################
        dict_psupp = Productsupply_parsing(pro)
        list_psupp.append(list(dict_psupp.values()))
        #################### Prices #######################
        if Psupp is not None:
            for pri in Psupp.findall('Price'):
                dict_pri = Prices(pro, pri)
                list_pri.append(list(dict_pri.values()))
    except AttributeError:
        print('the problem is in the list code ')
try:
    Xml_to_Mysql(list_prod, 'product', connection, prod_tuple)
except:
    print('query injection error')
