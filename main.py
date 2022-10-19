import tinypng_rs
import asyncio


# import uvloop
# uvloop.install()

async def main():
    a = await tinypng_rs.compress_image("lkhs48ZKmMpKG9WbcjJD5jpyFL8Lrn7z", "d:/1.png", "d:/2.png")
    print(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
