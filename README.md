# Geocoder & Elevation from Google Maps
##ARCPY100
Project | Ref 
--- | --- 
ArcPy| ARCPY100

<p>The tool is designed to obtain elevation,geocoder details for a given list of places in a CSV file from google map's web services and creates corresponding features in ArcGIS.<p>


### Editing Config.json

In order to modify the parameters involved in the process , edit the config.json in the assets folder.

```json
{
  "places":"Path/to/your/csv/file.csv",
  "delimiter":"<delimiter>",
  "environment":"Path/to/your/arcgis/environment.gdb",
  "poi1":"<First Filter to narrow down your search>",
  "poi2":"<Second Filter to narrow down your search>",
  "timeout":"<time out in seconds>",
  "featureclass":"<feature_class_name>"
}
```





