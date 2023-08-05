from mooscraper.openshift_v4 import rhcos

if __name__ == '__main__':
    for i in rhcos.get_sub_versions("s390x", "4.13"):
        print("ITEM: \n")
        print(i)
        print("")