cloudProviders={'AWS','GCP','AZURE'} #Sets are unordered collection of unique elements
print(cloudProviders)
cloudProviders.add('IBM')
cloudProviders.add('Oracle')
print(cloudProviders)
cloudProviders.remove('Oracle')
print(cloudProviders)