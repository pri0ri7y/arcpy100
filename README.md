# Geocoder & Elevation from Google Maps
##ARCPY100
<p>For information regarding the functionality , see <a href="http://pri0ri7y.github.io/About-Me/" target="_blank">here</a></p>
Project | Ref 
--- | --- 
ArcPy| ARCPY100


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





