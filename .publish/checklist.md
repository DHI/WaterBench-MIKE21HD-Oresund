# Publishing check list

## Folder structure

* input (dfs and mesh files for MIKE simulation)
* model (pfs/log files)
* observations (csv files)
* code 
* figures 
* output_sample (if output to big for repo)
* output 
* .preprocessing (hidden, also rawdata if possible)
* .publish (hidden)

## csv files

- Always use UTC, use "datetime_UTC" as name of col
- iso8601 format: 2014-01-01T00:00:00  (but tz naive)
- Only include relevant cols
- Avoid data with obvious rounding errors
- File name like: Altimetry_wl_6a.csv; Drogden_wl.csv etc (avoid time in filename)


## MIKE files




## Licenses

##