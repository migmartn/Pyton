import speedtest
test = speedtest.speedtest()
download = test.download()
upload = test.upload()

print(f"bajada: {download}")
print(f"subida: {upload}")