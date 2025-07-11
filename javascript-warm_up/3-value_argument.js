#!/usr/bin/node

const args = process.argv.slice(2);

if (args.lenght == 0)
    {
        console.log('No argument');
    }

    else
        {
            console.log(args);
        }