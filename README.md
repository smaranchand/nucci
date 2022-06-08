![Nucci](https://github.com/smaranchand/nucci/raw/main/nucci.gif)

Save your nuclei scan results to cloud.
Nucci is nothing but tool that lets you save your Nuclei tools output to the cloud database. Mongo.com provides a free database cluster which are we using to save the Nuclei scan  results.

Initially i had plan to create a GUI for Project discovery's nuclei tool but we tried to launch a very basic solution instead. The tool use stdout to read the output of the nuclei scan uses some regex to validate and sanitize as upload them to a mongo db instance. Later on the data can be fetched and browsed using a webapp.

