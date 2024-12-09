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
* .publish (hidden, contain all material/scripts necessary for publishing)

## csv files

- Always use UTC, use "datetime_UTC" as name of col
- iso8601 format: 2014-01-01T00:00:00  (but tz naive)
- Only include relevant cols
- Avoid data with obvious rounding errors
- File name like: Altimetry_wl_6a.csv; Drogden_wl.csv etc (avoid time in filename)


## Code

* Notebooks should be runnable (not raise Exceptions) with output sample data
* Include requirements.txt 


## MIKE files

* Start from hotfile if possible (to avoid spin-off period inside result); alternatively, include x number of days before Jan 1 to have spin-up outside result period
* Include both full-domain (state) output (dfsu) and point timeseries (dfs0) at observation points


## Licenses

* CC4 ??? 
* 


## Misc checks

* 


## Files for Zenodo

* CaseName.zip 
* CaseName-outputs.zip 
* README.pdf (rendered version )