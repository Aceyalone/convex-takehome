# This would be the main executing file for automating this data pipe
import pipe


#if we wanted to check out some of the data first without uploading:
data = pipe.build()
print(data.columns)
print(data.shape)
print(data.neighbourhood.value_counts())

# but for production we'd probably want to run it all with this line:
# (won't work bc no SQL server)
pipe.run()