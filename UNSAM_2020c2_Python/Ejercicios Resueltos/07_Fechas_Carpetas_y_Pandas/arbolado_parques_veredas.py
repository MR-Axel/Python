import pandas as pd
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt


def plot_dataset(dataset, variables):
    '''
    Plots de dataset generado
    '''
    dataset.boxplot(variables[0],by = 'ambiente')
    dataset.boxplot(variables[1],by = 'ambiente')
    plt.show()


def datasets (df_parques, df_veredas, tipos, cols):
    df_tipos_parques = df_parques[df_parques[cols[2]] == tipos[0]][cols[0:3]].copy()
    df_tipos_parques = df_tipos_parques.rename(columns={cols[0]: 'altura', cols[1]: 'diametro', cols[2]: 'nombre'})
    df_tipos_parques['ambiente'] = 'parque'

    df_tipos_veredas = df_veredas[df_veredas[cols[5]] == tipos[1]][cols[3:]].copy()
    df_tipos_veredas = df_tipos_veredas.rename(columns={cols[3]: 'altura', cols[4]: 'diametro', cols[5]: 'nombre'})
    df_tipos_veredas['ambiente'] = 'vereda'

    df_tipos = pd.concat([df_tipos_veredas, df_tipos_parques])
    print(df_tipos)

    return df_tipos


def main (veredas, parques):
    directorio = 'Data'
    fname_v = os.path.join(directorio, veredas)
    df_veredas = pd.read_csv(fname_v)
    fname_p = os.path.join(directorio, parques)
    df_parques = pd.read_csv(fname_p)

    tipos = ['Tipuana Tipu', 'Tipuana tipu']
    cols = ['altura_tot', 'diametro', 'nombre_cie', 'altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
    variables = ['diametro', 'altura']
    dataf = datasets(df_parques, df_veredas, tipos, cols)

    plot_dataset(dataf, variables)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            primer_archivo = sys.argv[1]
            segundo_archivo = sys.argv[2]
        else:
            primer_archivo = 'arbolado-publico-lineal-2017-2018.csv'
            segundo_archivo = 'arbolado-en-espacios-verdes.csv'
    except FileNotFoundError:
        print(f'No se encuentran los archivos')
    main(primer_archivo, segundo_archivo)









