![Nucci](https://github.com/smaranchand/nucci/raw/main/src/nucci.gif)

# RIP Internet Hero Binit Ghimire.

Nucci is nothing but tool that lets you save your Nuclei tools output to the cloud database. Mongo.com provides a free database cluster which are we using to save the Nuclei scan  results.

The tool uses stdin to read the output of the nuclei scan, uses some regex to sanitize and upload them to a mongo db instance. Later on the data can be fetched and browsed using a webapp developed in flask.

## WHY?

I created it so you dont have to.

## Configuration & Setup

### Database Setup:

A local database or cloud database can be used to store the nuclei results, [Mongodb.com](https://www.mongodb.com) provides a free database cluster which we can utilize.

1. Go to https://www.mongodb.com/cloud/atlas/register and complete the signup process.
2. Choose Shared plan.![Free Plan](https://github.com/smaranchand/nucci/blob/main/src/free.png)
3. Create database user.![Create Creds](https://github.com/smaranchand/nucci/blob/main/src/create_creds.png)
4. Enable Internet access so that we can access it from public IP, You can strict access to database if you have static IP address. ![Enable Access](https://github.com/smaranchand/nucci/blob/main/src/network.png)
5. Save the connection string to use in nucci.![Connection String](https://github.com/smaranchand/nucci/blob/main/src/db_connection.png)

### Alias Setup:

Nucci can be simply used by calling the ```read.py``` file after pipe. You can alias can be set in your ```.bashrc``` or ```.zshrc```
for now. We are planing to create a pip package for simplyfying.
```alias nucci="python /path/to/your/file/read.py"```

## Usage:

![help](https://github.com/smaranchand/nucci/raw/main/src/help.png)<br>

```console
nucci --config (Configure Mongodb)
nucci --webserver (Run a flask webserver to access dashboard)
```
### Save results
```cat sample_data.txt|nucci``` <br>
![cat](https://github.com/smaranchand/nucci/raw/main/src/cat.png)<br>
if alias not set <br>
```cat sample_data.txt|python3 path/to/your/file/nucci/read.py```

### View Results
 ```nucci --webserver ``` or ```python3 /nucci/webapp/webapp.py```
 ![dashboard](https://github.com/smaranchand/nucci/raw/main/src/dashboard.png)<br>

### Specaial Thanks and Shoutouts:

[Project discovery's Nuclei](https://github.com/projectdiscovery/nuclei)<br>
Yunish Shrestha<br>
Kailash Bohara<br>
Ankit Pandey<br>
Rohitash Kumar
