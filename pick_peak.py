def pick_peaks(arr):
    prvs, crrnt= 0, 0
    pstn ,peak= [], []
    for next in range(1, len(arr)):
        if arr[next] > arr[crrnt]:
            prvs = crrnt
            crrnt = next
        else:
           if arr[next] < arr[crrnt]:
              if arr[prvs] < arr[crrnt]:
                 pstn.append(crrnt)
                 peak.append(arr[crrnt])
              prvs = crrnt
              crrnt = next
    return {"pos": pstn, "peaks": peak}