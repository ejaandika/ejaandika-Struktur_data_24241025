class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_data(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def hapus_awal(self):
        if not self.head:
            print("List kosong")
            return
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del temp

    def hapus_akhir(self):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        if not current.next:
            self.head = None
            del current
            return
        while current.next:
            current = current.next
        current.prev.next = None
        del current

    def hapus_berdasarkan_nilai(self, nilai):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        while current:
            if current.data == nilai:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                del current
                print(f"Node dengan nilai {nilai} berhasil dihapus")
                return
            current = current.next
        print(f"Node dengan nilai {nilai} tidak ditemukan")

    def tampilkan(self):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        print("Isi Linked List:")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Contoh Penggunaan
dll = DoubleLinkedList()
dll.tambah_data(10)
dll.tambah_data(20)
dll.tambah_data(30)
dll.tampilkan()

dll.hapus_awal()
dll.tampilkan()

dll.hapus_akhir()
dll.tampilkan()

dll.hapus_berdasarkan_nilai(20)
dll.tampilkan()