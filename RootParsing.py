from Functions import Default

def Product_Parsing(root):
    dict_prod={}
    Desc = root.find('DescriptiveDetail')
    try:
        dict_prod['ISBN'] = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        dict_prod['GTIN'] = Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        dict_prod['RefIntern'] = Default(root, './ProductIdentifier[ProductIDType="01"]/IDValue')
        dict_prod['Title'] = Default(root, './DescriptiveDetail/TitleDetail[TitleType="01"]/TitleElement/TitleText')
        dict_prod['ImprintName'] =Default(root,'./PublishingDetail/Imprint/ImprintName')
        dict_prod['Distributor'] = Default(root, './ProductSupply/SupplyDetail/Supplier/SupplierName')
        dict_prod['Price'] = Default(root, './ProductSupply/SupplyDetail/Price/PriceAmount')
        dict_prod['TextType']=Default(root,'./CollateralDetail/TextContent/TextType')
        dict_prod['ContentAudience']=Default(root,'./CollateralDetail/TextContent/ContentAudience')
        dict_prod['Text']=Default(root,'./CollateralDetail/TextContent/Text')
        dict_prod['BarcodeType'] = Default(root, './Barcode/BarcodeType')
        dict_prod['PositionOnProduct'] = Default(root, './Barcode/PositionOnProduct')
    except AttributeError:
        None
    except SyntaxError:
        print("Product Parsing error")
    return dict_prod

def DescDetail_Parsing(root):
    dict_desc = {}
    try:
        Desc = root.find('DescriptiveDetail')
        collect=Desc.find('Collection')
        ID1=Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2=Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_desc['ISBN'] = ID2
        elif ID2 is None:
            dict_desc['ISBN']=ID1
        else:
            dict_desc['ISBN']=None
        dict_desc['ProductComposition'] = Default(Desc, './ProductComposition')
        dict_desc['ProductForm'] = Default(Desc, './ProductForm')
        dict_desc['Measurement_01'] = Default(Desc, './Measure[MeasureType="01"]/Measurement')
        dict_desc['MeasureUnit_01'] = Default(Desc, './Measure[MeasureType="01"]/MeasureUnitCode')
        dict_desc['Measurement_02'] = Default(Desc, './Measure[MeasureType="02"]/Measurement')
        dict_desc['MeasureUnit_02'] = Default(Desc, './Measure[MeasureType="02"]/MeasureUnitCode')
        dict_desc['Measurement_03'] = Default(Desc, './Measure[MeasureType="03"]/Measurement')
        dict_desc['MeasureUnit_03'] = Default(Desc, './Measure[MeasureType="03"]/MeasureUnitCode')
        dict_desc['Measurement_08'] = Default(Desc, './Measure[MeasureType="08"]/Measurement')
        dict_desc['MeasureUnit_08'] = Default(Desc, './Measure[MeasureType="08"]/MeasureUnitCode')
        dict_desc['ProdClassificationType'] = Default(Desc, './ProductClassification/ProductClassificationType')
        dict_desc['ProdClassificationCode ']= Default(Desc, './ProductClassification/ProductClassificationCode')
        dict_desc['CLType'] = Default(collect, './CollectionType')
        dict_desc['CLTitleElemLevel_01'] = Default(collect, './TitleDetail[TitleType="01"]/TitleElement/TitleElementLevel')
        dict_desc['CLTitleText_01'] = Default(collect, './TitleDetail[TitleType="01"]/TitleElement/TitleText')
        dict_desc['CLTitleElemLevel_05'] = Default(collect, './TitleDetail[TitleType="05"]/TitleElement/TitleElementLevel')
        dict_desc['CLTitleText_05'] = Default(collect, './TitleDetail[TitleType="05"]/TitleElement/TitleText')
        dict_desc['TitleElemLevel_01'] = Default(collect, './TitleDetail[TitleType="01"]/TitleElement/TitleElementLevel')
        dict_desc['TitleText_01'] = Default(Desc, './TitleDetail[TitleType="01"]/TitleElement/TitleText')
        dict_desc['TitleElemLevel_05'] = Default(Desc, './TitleDetail[TitleType="05"]/TitleElement/TitleElementLevel')
        dict_desc['TitleText_05'] = Default(Desc, './TitleDetail[TitleType="05"]/TitleElement/TitleText')
        dict_desc['TitleElemLevel_10'] = Default(Desc, './TitleDetail[TitleType="10"]/TitleElement/TitleElementLevel')
        dict_desc['TitleText_10'] = Default(Desc, './TitleDetail[TitleType="10"]/TitleElement/TitleText')
        dict_desc['LanguageRole'] = Default(Desc, './Language/LanguageRole')
        dict_desc['LanguageCode'] = Default(Desc, './Language/LanguageCode')
        dict_desc['ExtentType']=Default(Desc,'./Extent/ExtentType')
        dict_desc['ExtentValue']=Default(Desc,'./Extent/ExtentValue')
        dict_desc['ExtentUnit'] = Default(Desc, './Extent/ExtentUnit')
        dict_desc['AudienceCodeType'] = Default(Desc, './Audience/AudienceCodeType')
        dict_desc['AudienceCodeValue'] = Default(Desc, './Audience/AudienceCodeValue')
        dict_desc['AudienceRangeQualifier'] = Default(Desc, './AudienceRange/AudienceRangeQualifier')
        dict_desc['AudienceRangePrecision_01'] = Default(Desc, './AudienceRange[1]/AudienceRangePrecision')
        dict_desc['AudienceRangeValue_01'] = Default(Desc, './AudienceRange[1]/AudienceRangeValue')
        dict_desc['AudienceRangePrecision_02'] = Default(Desc, './AudienceRange[2]/AudienceRangePrecision')
        dict_desc['AudienceRangeValue_02'] = Default(Desc, './AudienceRange[2]/AudienceRangeValue')
    except SyntaxError:
        print("DescriptiveDetail Parsing error")
    except AttributeError:
        None
    return dict_desc

def Contributor_parsing(root,cont):
    dict_cont={}
    try:
        ID1 = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2 = Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_cont['ISBN'] = ID2
        elif ID2 is None:
            dict_cont['ISBN'] = ID1
        else:
            dict_cont['ISBN'] = None
        dict_cont['SequenceNumber'] = Default(cont, './SequenceNumber')
        dict_cont['ContributorRole'] = Default(cont, './ContributorRole')
        dict_cont['PersonName'] = Default(cont, './PersonName')
        dict_cont['KeyNames'] = Default(cont, './KeyNames')
    except AttributeError:
        None
    except SyntaxError:
        print("Contributor Parsing error")
    return dict_cont

def Subject_parsing(root,Sub):
    dict_subj={}
    try:
        ID1=Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2=Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_subj['ISBN'] = ID2
        elif ID2 is None:
            dict_subj['ISBN']=ID1
        else:
            dict_subj['ISBN']=None
        dict_subj['SubjectSchemeIdentifier'] = Default(Sub, './SubjectSchemeIdentifier')
        dict_subj['SubjectCode'] = Default(Sub, './SubjectCode')
        dict_subj['SubjectHeadingText'] = Default(Sub, './SubjectHeadingText')
    except AttributeError:
        None
    except SyntaxError:
        print("Subject Parsing error")
    return dict_subj

def SuppResources_parsing(root,Res):
    dict_supp = {}
    try:
        ID1 = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2 = Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_supp['ISBN'] = ID2
        elif ID2 is None:
            dict_supp['ISBN'] = ID1
        else:
            dict_supp['ISBN'] = None
        dict_supp['ResourceContentType'] = Default(Res, './ResourceContentType')
        dict_supp['ContentAudience'] = Default(Res, './ContentAudience')
        dict_supp['ResourceMode'] = Default(Res, './ResourceMode')
        dict_supp['ResourceForm'] = Default(Res, './ResourceVersion/ResourceForm')
        dict_supp['FeatureValue_04'] = Default(Res,'./ResourceVersion/ResourceVersionFeature[ResourceVersionFeatureType="04"]/FeatureValue')
        dict_supp['FeatureValue_01'] = Default(Res,'./ResourceVersion/ResourceVersionFeature[ResourceVersionFeatureType="01"]/FeatureValue')
        dict_supp['FeatureValue_02'] = Default(Res,'./ResourceVersion/ResourceVersionFeature[ResourceVersionFeatureType="02"]/FeatureValue')
        dict_supp['FeatureValue_03'] = Default(Res,'./ResourceVersion/ResourceVersionFeature[ResourceVersionFeatureType="03"]/FeatureValue')
        dict_supp['FeatureValue_07'] = Default(Res,'./ResourceVersion/ResourceVersionFeature[ResourceVersionFeatureType="07"]/FeatureValue')
        dict_supp['ResourceLink'] = Default(Res, './ResourceVersion/ResourceLink')
        dict_supp['ContentDateRole'] = Default(Res, './ResourceVersion/ContentDate/ContentDateRole')
        dict_supp['DateFormat'] = Default(Res, './ResourceVersion/ContentDate/DateFormat')
        dict_supp['Date'] = Default(Res, './ResourceVersion/ContentDate/Date')
    except AttributeError:
        None
    except SyntaxError:
        print("SuppResources Parsing error")
    return dict_supp

def PublishDetail_parsing(root):
    dict_pub = {}
    try:
        Pub=root.find('PublishingDetail')
        Imp=Pub.find('Imprint')
        ID1 = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2 = Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_pub['ISBN'] = ID2
        elif ID2 is None:
            dict_pub['ISBN'] = ID1
        else:
            dict_pub['ISBN'] = None
        dict_pub['ImprintIDType'] =Default(Imp,'./ImprintIdentifier/ImprintIDType')
        dict_pub['IDValue'] =Default(Imp,'./ImprintIdentifier/IDValue')
        dict_pub['ImprintName'] =Default(Imp,'./ImprintName')
        dict_pub['PublishingRole'] =Default(Pub,'./Publisher/PublishingRole')
        dict_pub['PublisherName'] =Default(Pub,'./Publisher/PublisherName')
        dict_pub['DateFormat_R01'] =Default(Pub,'./PublishingDate[PublishingDateRole="01"]/DateFormat')
        dict_pub['Date_R01'] =Default(Pub,'./PublishingDate[PublishingDateRole="01"]/Date')
        dict_pub['DateFormat_R13'] =Default(Pub,'./PublishingDate[PublishingDateRole="13"]/DateFormat')
        dict_pub['Date_R13'] =Default(Pub,'./PublishingDate[PublishingDateRole="13"]/Date')
    except AttributeError:
        None
    except SyntaxError:
        print("PublishDetail Parsing error")
    return dict_pub

def RelatedMaterial(root):
    dict_rel={}
    try:
        ID1=Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2=Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_rel['ISBN'] = ID2
        elif ID2 is None:
            dict_rel['ISBN']=ID1
        else:
            dict_rel['ISBN']=None
        dict_rel['SubjectSchemeIdentifier'] = Default(root, './RelatedProduct/')
        dict_rel['SubjectCode'] = Default(root, './SubjectCode')
        dict_rel['SubjectHeadingText'] = Default(root, './SubjectHeadingText')
    except AttributeError:
        None
    except SyntaxError:
        print("Subject Parsing error")
    return dict_rel

def Productsupply_parsing(root):
    dict_ps = {}
    try:
        Psupp = root.find('ProductSupply')
        Detail = Psupp.find('SupplyDetail')
        ID1 = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2 = Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_ps['ISBN'] = ID2
        elif ID2 is None:
            dict_ps['ISBN'] = ID1
        else:
            dict_ps['ISBN'] = None
        dict_ps['ISBN'] = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        dict_ps['RegionsIncluded'] = Default(Psupp, './Market/Territory/RegionsIncluded')
        dict_ps['CountriesExcluded'] = Default(Psupp, './Market/Territory/CountriesExcluded')
        dict_ps['SupplierRole'] = Default(Detail, './Supplier/SupplierRole')
        dict_ps['SupplierIDType'] = Default(Detail, './Supplier/SupplierIdentifier/SupplierIDType')
        dict_ps['IDValue'] = Default(Detail, './Supplier/SupplierIdentifier/IDValue')
        dict_ps['SupplierName'] = Default(Detail, './Supplier/SupplierName')
        dict_ps['ReturnsCodeType'] = Default(Detail, './ReturnsConditions/ReturnsCodeType')
        dict_ps['ReturnsCode'] = Default(Detail, './ReturnsConditions/ReturnsCode')
        dict_ps['ProductAvailability'] = Default(Detail, './ProductAvailability')
        dict_ps['SupplyDateRole'] = Default(Detail, './SupplyDate/SupplyDateRole')
        dict_ps['DateFormat'] = Default(Detail, './SupplyDate/SupplyDateRole')
        dict_ps['Date'] = Default(Detail, './SupplyDate/SupplyDateRole')
        dict_ps['ItemPriceState'] = Default(Psupp, './ProductIdentifier[ProductIDType="15"]/IDValue')
    except AttributeError:
        None
    except SyntaxError:
        print("ProductSupply Parsing error")
    return dict_ps

def Prices(root,pri):
    dict_pri = {}
    try:
        Psupp = root.find('ProductSupply')
        SDetail = Psupp.find('SupplyDetail')
        ID1 = Default(root, './ProductIdentifier[ProductIDType="15"]/IDValue')
        ID2 = Default(root, './ProductIdentifier[ProductIDType="03"]/IDValue')
        if ID1 is None:
            dict_pri['ISBN'] = ID2
        elif ID2 is None:
            dict_pri['ISBN'] = ID1
        else:
            dict_pri['ISBN'] = None
        dict_pri['PriceType'] = Default(pri, './PriceType')
        dict_pri['DiscountCodeType'] = Default(pri, './DiscountCoded/DiscountCodeType')
        dict_pri['DiscountCodeTypeName'] = Default(pri, './DiscountCoded/DiscountCodeTypeName')
        dict_pri['DiscountCode'] = Default(pri, './DiscountCoded/DiscountCode')
        dict_pri['PriceStatus'] = Default(pri, './PriceStatus')
        dict_pri['PriceAmount'] = Default(pri, './PriceAmount')
        dict_pri['TaxType'] = Default(pri, './Tax/TaxType')
        dict_pri['TaxRateCode'] = Default(pri, './Tax/TaxRateCode')
        dict_pri['TaxRatePercent'] = Default(pri, './Tax/TaxRatePercent')
        dict_pri['TaxableAmount'] = Default(pri, './Tax/TaxableAmount')
        dict_pri['TaxAmount'] = Default(pri, './Tax/TaxAmount')
        dict_pri['CurrencyCode'] = Default(pri, './CurrencyCode')
        dict_pri['RegionsIncluded']=Default(pri,'./Territory/RegionsIncluded')
        dict_pri['CountriesExcluded']=Default(pri,'./Territory/CountriesExcluded')
    except AttributeError:
        None
    except SyntaxError:
        print("Prices Parsing error")
    return dict_pri