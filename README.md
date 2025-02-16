# IPFS
## Automated scripts
1. ipfs desktop
2. pinata
## To check ipfs version
```
ipfs version
```
### `or` if ipfs is not working in cmd:-
"C:\Users\ASUS\AppData\Local\Programs\IPFS Desktop\resources\app.asar.unpacked\node_modules\kubo\kubo\ipfs.exe" version

you will get version
```
ipfs version 0.33.1
```
## To solve this problem(if you had installed window/updated version)
1. install ipfs
2. open environment variable ->Advanced ->Environment variable (click) ->(system variable (path)->edit
3. new->C:\Users\ASUS\AppData\Local\Programs\IPFS Desktop\resources\app.asar.unpacked\node_modules\kubo\kubo\
4. ok

## start garbage collector
ipfs repo gc

<!-- # use this URL to access ipfs
`https://dweb.link/ipfs/<hash>`

example:-
`https://dweb.link/ipfs/QmXQh5Pvu6jGse73pawMDKBXr3CMjWqLPw8bWbuqye4P4S` -->


# run html in server
```cmd
python -m http.server 8000
```
