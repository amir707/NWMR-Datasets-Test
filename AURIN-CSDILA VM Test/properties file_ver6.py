-----------------------------
# version 6- Prepration Date 13 Nov 16:30
# Properties specific to the NWMR data provider
#

# Geoserver test instance settings
gs.path=http://192.43.209.39:8080/geoserver
gs.user=aurin
gs.password=aurinaccess
gs.workspace=nwmr
gs.test.datastore=GIS_Database

# Test properties
# Geometry attribute common to all layers
gs.test.geomattribute=the_geom

# Layer on which to perform selection tests and non-geometric attributes to return
gs.test.layer=BH2010_P
gs.test.attributes=lotsperha,totallots

# Attribute and value for attribute query (should return only one feature)
gs.test.areanameattribute=siteid
gs.test.areanamevalue=100009

# Bounding box that should contain no features
gs.test.emptybbox=1,0,10,10
gs.test.emptybboxnfeatures=0

# Bounding box and number of returned features for bbox query
gs.test.bbox=-38.388659,146.045925,-37.926616,146.916513
gs.test.bboxnfeatures=120

# Polygon definition in WKT and number of returned features for polygon query
gs.test.polygon=POLYGON(( -37.338065 143.680993 ,-37.340117 143.937473 ,-37.586338
144.027754, -37.842818 143.865658, -37.844870 143.642008, -37.549405 143.564038 ,
  -37.338065 143.680993))
gs.test.polygonnfeatures=124

# Point that returns one feature when a point query is performed
gs.test.point=POINT(-38.282679 144.486310)

# ID of dataset in Data Registration Service (leave it as it is for the time being)
gs.test.dataproviderid=333333

# Layers to test
# Comma-separated list of all layers to check for existence
gs.test.layers=Property_Value_5LGA,UGB_2010_polygon_object,MRS2010,MINOR_INFILL_SUPPLY2009_P,MAJOR_INFILL2009_P,IND2010_Proposed_Areas,IND2010_Nodes,IND2010,BH2010_Estates,BH2010_P,tblStop_TimeTable_join,stopinformation_victoria,com_predominant_landuse,com_capacities_2008,com_capacities_2010,com_m2spaceuse_2008,com_m2spaceuse_2010,com_emplbyindustry_2008,com_emplbyindustry_2010,public_street_light_melton,footpaths_melton,ptv_stationentriestransfer,Tram_Origin_Des_Survey_2011,Affordable_Lettings_by_LGA_June2012_1bdr,Affordable_Lettings_by_LGA_June2012_2bdr,Affordable_Lettings_by_LGA_June2012_3bdr,Affordable_Lettings_by_LGA_June2012_4bdr,Affordable_Lettings_by_LGA_June2012_total,Cordon_Station_Average_Load_by_Service_May2012,Quarterly_Median_Rents_by_LGA_June2012_1bdr_flat,Quarterly_Median_Rents_by_LGA_June2012_2bdr_flat,Quarterly_Median_Rents_by_LGA_June2012_2bdr_house,Quarterly_Median_Rents_by_LGA_June2012_3bdr_house,Quarterly_Median_Rents_by_LGA_June2012_4bdr_house

# Comma separated list of layer_name:n_of_geometries for some selected layers
gs.test.ngeoms=UGB_2010_polygon_object:1,MRS2010:1821,MINOR_INFILL_SUPPLY2009_P:2082,MAJOR_INFILL2009_P:154,IND2010_Proposed_Areas:14,IND2010_Nodes:6,BH2010_Estates:275,BH2010_P:1965,com_predominant_landuse:14108,com_capacities_2008:606,com_capacities_2010:606,com_m2spaceuse_2008:606,com_m2spaceuse_2010:606,com_emplbyindustry_2008:606,com_emplbyindustry_2010:606,public_street_light_melton:2397,footpaths_melton:9029,ptv_stationentriestransfer:208,Tram_Origin_Des_Survey_2011:7958,Affordable_Lettings_by_LGA_June2012_1bdr:80,Affordable_Lettings_by_LGA_June2012_2bdr:80,Affordable_Lettings_by_LGA_June2012_3bdr:80,Affordable_Lettings_by_LGA_June2012_4bdr:80,Affordable_Lettings_by_LGA_June2012_total:80,Cordon_Station_Average_Load_by_Service_May2012:893,Quarterly_Median_Rents_by_LGA_June2012_1bdr_flat:94,Quarterly_Median_Rents_by_LGA_June2012_2bdr_flat:95,Quarterly_Median_Rents_by_LGA_June2012_2bdr_house:79,Quarterly_Median_Rents_by_LGA_June2012_3bdr_house:95,Quarterly_Median_Rents_by_LGA_June2012_4bdr_house:95
#Property_Value_5LGA:197862, stopinformation_victoria:26849,IND2010:81909,tblStop_TimeTable_join:1323000,stopinformation_victoria:26849