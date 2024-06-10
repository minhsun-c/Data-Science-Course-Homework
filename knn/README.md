`analyze.ipynb`: 分析 `Wine Dataset`, `20 Newsgroup Dataset` 的過程

`breast_cancer.ipynb`: 分析 `Breast Cancer Wisconsin (Diagnostic) Dataset` ，並以此資料集訓練和預測


# 分析資料集

最終選擇使用 `Breast Cancer Wisconsin (Diagnostic) Dataset` 。因為從散佈圖可以看到這個資料集可以將資料點很完美的分成兩群，中間僅有很少數的資料點重疊。適合用 KNN 來分析。

`Wine Dataset` 雖然也可以不錯的分群，但是重疊的資料點相對 `Breast Cancer Wisconsin (Diagnostic) Dataset` 來說，還是相對多。

`20 Newsgroup Dataset` 由於是非數字資料，需要先向量化，再者其維度較高，需要再行處理。最終從散佈圖中可以看到他有不少資料點的重疊，且資料種類相對多，不容易透過 KNN 分辨。

---

# KNN

在預測 `Breast Cancer` 時，我使用兩類型的特徵：癌細胞大小相關、癌細胞質地相關。大小相關的參數包含radius, area, perimeter等。質地相關的參數包含 texture, smoothness 。

我也測試是否要先預處理資料，使用的是 `StandardScaler`，結果發現預處理後的資料集，在預測上的準確度較高。 

最終結果是「任意大小相關參數」、「任意質地相關參數」搭配標準化後的資料集，準確度皆高達 96% 。其中，k = 5~9 皆為不錯的選擇。其餘數值皆有相同的趨勢，以標準化後的資料有較好的表現。


