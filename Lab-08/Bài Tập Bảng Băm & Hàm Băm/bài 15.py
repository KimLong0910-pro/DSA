class ConsistentHash:
    def __init__(self):
        self.servers = []

    def add_server(self, vi_tri):
        self.servers.append(vi_tri)
        self.servers.sort()

    def get_server(self, khoa):
        if not self.servers:
            return None

        hash_value = hash(khoa) % 360

        for vi_tri in self.servers:
            if vi_tri >= hash_value:
                return vi_tri

        return self.servers[0]


hash_ring = ConsistentHash()
hash_ring.add_server(50)
hash_ring.add_server(150)
hash_ring.add_server(300)

print(f"Apple -> Server tại vị trí {hash_ring.get_server('apple')}")
print(f"Banana -> Server tại vị trí {hash_ring.get_server('banana')}")