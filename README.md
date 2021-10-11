# tbot - Telegram Ecommerce Chatbot

The bot offers to order products from the [products.csv](https://github.com/ABorovtsov/tbot/blob/main/data/products.csv) file. All the orders are registered in the [orders.csv](https://github.com/ABorovtsov/tbot/blob/main/data/orders.csv). Eat more chocolate and have fun!

# Run in container

1. Go to the folder with the source code:

```powershell
cd %Src_Folder%
```

2. Build the image:
```powershell
docker build -t aborovtsov/tbot:v0.1.0 .
```

3. Run the container:
```powershell
docker run --rm -it -p 8000:8000 --name tbot aborovtsov/tbot
```