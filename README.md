# [PyCon APAC 2022] <br> 從開放數據閱讀台灣能源 - 數據探索、模型預測和風險評估 

## 摘要
能源預測和不確定性風險評估一直是業界和學術上熱門的議題, 尤其他們與碳排放減量和能源供應等等的實際議題相關。在台灣, 各式各樣的開放數據已經對外公布了數年, 已累積不少的良好應用案例。與能源相關的開放數據更是累積了超過五年以上, 包含用電、氣象和行事曆等。然而對於這些能源數據的深入分析和模型實際應用卻不是相當常見, 多半只停留在少數的學校論文探討之中。為了展示能源開放數據的應用潛力, 本演講將會用python實踐數據爬取(Data scrpaing)和建立常見的機器學習模型, 以及從數據挖掘有價值的觀點和應用潛力。將會從簡單的Explorative Data Analysis(EDA)開始, 藉由資料視覺化和敘述統計分析能源數據的性質。接著, 由氣象預報和行事曆建立能源預測模型, 並比較模型和台電API的預測準確度。除了藉此案例宣傳能源開放數據的潛力外, 也預計帶給聽眾python應用於數據模型專案的常用工具和經驗分享。

## 說明
台灣的開放數據平台已經行之有年, 關於能源的供需都累積了超過五年的充足數據量可供應用。此外, 作為影響能源的重要變因, 如氣象數據和行事曆數據, 也都分別可以在開放數據平台取得。因此, 以這些充足的數據為基礎, 台灣的能源數據應用具有相當好的潛力, 尤其以能源預測和風險管理又最為重要。由於供電能力需要根據隔日預測做好電廠的排程, 過大的供電能力會造成電力浪費、過小的供電能力則會讓電網有斷電的風險。而近年來的電力能源問題時常浮出檯面, 台電供電能力時常受到質疑。因此, 本演講將以台灣能源的可預測性和不確定性的風險評估作為主軸, 和台電的能源預測評估作性能比較。另外, 也向聽眾宣傳台灣能源數據的來源和可應用的潛力。

目前既有的開放數據集，包括了來自台灣北中南東四區的逐十分鐘的台電能源數據、台灣各縣市的氣象站數據、和人事行政局提供的行事曆數據。此外，作者也有存取了超過一年的氣象預報和能源預報數據，可以做為測試模型應用潛力的比較對象。這些數據來源有些是來自政府資料開放平臺的官方API，有些來自於網站界接前台視覺呈現的API，爬取過程和python中常用到的工具也都會一併介紹。除了能源和氣象數據高度相關, 溫度越高會造成用電量的攀升之外, 能源和人的行為也有密切關係, 國定假日和平日也都會有用電行為的差異。此演講將以這些數據集進行預測模型的建構。建立預測模型之前, 會先進行資料的探索性分析, 透過視覺化和統計成果讓聽眾了解能源和氣象與人員行為的關連性。根據對數據的了解, 會建立以氣象數據和人員行為為因子的預測模型。 並以保留一年的能源數據作為驗證, 評估模型的誤差及預測不確定性。這些誤差和不確定性也會與台電的API預測性能作比較。最後, 以能源模型預測的成果準確度作為結尾, 提出台電的預測服務是否有應用其他開放數據的潛力。並且在考慮預測不確定性的風險下, 台電的預測服務是否有進步的空間。

## 數據集
[壓縮檔 data.rar](https://github.com/PatrickFu0302/pycon2022_taiwan_energy/blob/main/data.rar)內包含:
- forecast: 氣象預報和台電須量預測的歷史數據 (2021.05-2022.07)
- loadarea: 區域用電的歷史數據(2017-2022)
- weatherData: 天氣的歷史數據(2017-2022)
