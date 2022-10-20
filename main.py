import tinypng_rs
import asyncio


async def compress(input, output):
    return await tinypng_rs.compress_image("lkhs48ZKmMpKG9WbcjJD5jpyFL8Lrn7z", input, output)


async def main():
    in_png = ["d:/test/1.jpg", "d:/test/2.jpg"]
    out_png = ["d:/test/1_1.jpg", "d:/test/2_2.jpg"]

    tasks = []
    for (i, o) in zip(in_png, out_png):
        tasks.append((i, asyncio.create_task(compress(i, o))))

    for (file, task) in tasks:
        try:
            a = await task
            print(f"file:{file} {a[0]}->{a[1]}")
        except IOError as e:
            print(e)
        finally:
            print("---------------")


if __name__ == '__main__':
    asyncio.run(main())
    pass
