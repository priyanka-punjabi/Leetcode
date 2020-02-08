class SnapshotArray:
    def __init__(self, length: int):
        self.snapshot_arr = dict()
        self.snaps = dict()
        self.snapCnt = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot_arr[index] = val

    def snap(self) -> int:
        self.snaps[self.snapCnt] = dict(self.snapshot_arr)
        self.snapCnt += 1
        return self.snapCnt - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        return 0