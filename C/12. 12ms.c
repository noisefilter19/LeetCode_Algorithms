int** transpose(int** A, int ARowSize, int *AColSizes, int** columnSizes, int* returnSize) {
    int **B = (int **)malloc(sizeof(int *) * (*AColSizes));
    for(int i = 0 ; i < *AColSizes; i++) *(B + i) = (int *)malloc(sizeof(int) * ARowSize);
    *columnSizes = (int *)malloc(sizeof(int) * (*AColSizes));
    for(int i = 0 ; i < *AColSizes; i++) *(*columnSizes + i) = ARowSize;
    for(int ColIdx = 0; ColIdx < *AColSizes; ColIdx++){
        for(int RowIdx = 0; RowIdx < ARowSize; RowIdx++){
            *(*(B + ColIdx) + RowIdx) = *(*(A + RowIdx) + ColIdx);
        }
    }
    *returnSize = *AColSizes;
    return B;
}
