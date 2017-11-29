Проверка для 2ого задания

    printf("%d %d   ", mass_Mn_1[0][0], mass_Mn_1[0][1]);
    printf("%d %d \n", mass_Mn_2[0][0], mass_Mn_2[0][1]);
    printf("%d %d   ", mass_Mn_1[1][0], mass_Mn_1[1][1]);
    printf("%d %d \n", mass_Mn_2[1][0], mass_Mn_2[1][1]);



int d;
      int t;
      for (d=0;d<2;d++)
      {
          for (t=0;t<2;t++)
          {
              printf("%d \n", Matrixmultiplication[d][t]);
          }
      }



void Matrixmultiplication (int massA[2][2], int massB[2][2])
{

      int massMultiplication[2][2];

      massMultiplication[0][0] = massA[0][0] * massB[0][0] + massA[0][1] * massB[1][0];
      massMultiplication[0][1] = massA[0][0] * massB[0][1] + massA[0][1] * massB[1][1];
      massMultiplication[1][0] = massA[1][0] * massB[0][0] + massA[1][1] * massB[1][0];
      massMultiplication[1][1] = massA[1][0] * massB[0][1] + massA[1][1] * massB[1][1];

      int i;
      int j;
      for (i=0;i<2;i++)
      {
          for (j=0;j<2;j++)
          {
              printf("%d", massMultiplication[i][j]);
          }
      }

}
