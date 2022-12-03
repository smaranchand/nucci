![Nucci](https://github.com/smaranchand/nucci/raw/main/src/nucci.gif)

#RIP Internet Hero Binit Ghimire.

Save your nuclei scan results to cloud.
Nucci is nothing but tool that lets you save your Nuclei tools output to the cloud database. Mongo.com provides a free database cluster which are we using to save the Nuclei scan  results.

Initially i had plan to create a GUI for Project discovery's nuclei tool but we tried to launch a very basic solution instead. The tool use stdout to read the output of the nuclei scan uses some regex to validate, sanitize and upload them to a mongo db instance. Later on the data can be fetched and browsed using a webapp developed using flask.


## WHY?

I created so you dont have to.

## Configuration & Setup

### Database Setup:

A local database or cloud database can be used to store the nuclei results, [Mongodb.com](https://www.mongodb.com) provides a free database cluster which are we going to utilize.

1. Go to https://www.mongodb.com/cloud/atlas/register and complete the signup process.
2. Choose Shared plan.![Free Plan](https://github.com/smaranchand/nucci/blob/main/src/free.png)
3. Create database user.![Create Creds](https://github.com/smaranchand/nucci/blob/main/src/create_creds.png)
4. Enable Internet access so that we can access it from public IP, You can strict access to database if you have static IP address. ![Enable Access](https://github.com/smaranchand/nucci/blob/main/src/network.png)
5. Save the connection string to use in nucci.![Connection String](https://github.com/smaranchand/nucci/blob/main/src/db_connection.png)

### Alias Setup:

Nucci can be simply used by calling the ```read.py``` file after appending pipe. For now an alias can be set in your ```.bashrc``` or ```.zshrc```

```alias nucci="python /path/to/your/file/read.py"```

## Usage:
```console
nucci -config run (Configure mongodb)
nucci -web run (Run a flask webserver to visualize the results.)

```
### Save results
```cat live_urls.txt|nuclei -t ~/nuclei-templates|nucci``` <br>
if alias not set <br>
```cat live_urls.txt|nuclei -t ~/nuclei-templates|python3 path/to/your/file/nucci/read.py```

### View Results
 ```nucci -web run``` or ```python3 /nucci/webapp/webapp.py```

### Specaial Thanks and Shoutouts:

[Project discovery's Nuclei](https://github.com/projectdiscovery/nuclei)<br>
Yunish Shrestha