import json

class avlController:
    def __init__(self):
        self.avl_data = self.loadData()

    def loadData(self):
        with open('avlIds.json') as f:
            data = json.load(f)
        return data

    def getAvlInfo(self, id):
        try:
            data = self.avl_data[id]
            return data
        except:
            print("id not found")
            return -1

if __name__ == "__main__":
    data = avlController()
    # print(data.avl_data)
    print(data.getAvlInfo("4"))
    print(data.getAvlInfo("1"))