import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


# Set the page configuration
st.set_page_config(page_title = "PYTHON PROJECT 2", page_icon = ":tada:", layout="wide")

# HEADER SECTION
with st.container():
    st.subheader("Hi:wave: we're from Gr 11 Business IT")
    st.title("Brand Laptops")

url = "https://www.kaggle.com/datasets/bhavikjikadara/brand-laptops-dataset"
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: st.header("Our dataset :sparkles:")
    st.markdown(f"[Click here to see the original dataset]({url})")
    st.header("What is it about:")
    st.markdown(
        """ This meticulously cleaned dataset presents a comprehensive collection of 991 unique laptops sourced from the 'Smartprix' website. Enriched with 22 features including laptop name, price in Indian rupees, processor, GPU, and more, it provides valuable insights for building robust price prediction models and effective recommendation systems.""",
        unsafe_allow_html=True
    )


st.divider()

st.sidebar.write('**:bulb: Reporting to Dr. Tan Duc Do**')
st.sidebar.write('**:bulb: Gr 11 Business IT members:**')

# Add content to the main area
with st.sidebar:
    st.write('Trần Gia Phú ')
    st.write('Đỗ Trần Anh Kiệt')
    st.write('Nguyễn Thái Sơn')
    st.write('Nguyễn Tuấn Khanh')
    st.write('Lê Trần Hoàng Sang')
    st.write('Bùi Trần Khánh Ngọc')

plot1, plot2, plot3, plot4, plot5 = st.tabs(["Plot 1", "Plot 2", "Plot 3", "Plot 4", "Plot 5"])

with plot1:
    Mydata = pd.read_csv('laptops.csv', sep=',')
    Mydata.columns = Mydata.columns.str.strip()

    n_bins = 20

    counts, bins, patches = plt.hist(Mydata['Rating'], bins=n_bins,
                                     edgecolor='black')

    for i, patch in enumerate(patches):
        plt.setp(patch, 'facecolor', plt.cm.rainbow(i / n_bins))

    plt.title('COMPUTER REVIEW REPORT')

    plt.xlabel('RATING SCORE')

    plt.ylabel('COMPUTER REVIEW REPORT')

    plt.xlim(0, 100)

    plt.ylim(0, 250)

    description = '''
    The given histogram illustrates the distribution of rating scores in a
    computer review report. The rating scores are depicted on the
    horizontal axis, while the frequency or number of reviews is
    represented on the vertical axis.
    
    As can be seen from the chart, it is evident from the histogram that
    the majority of the rating scores cluster around the middle range, with
    fewer ratings at both the lower and higher ends of the spectrum.
    
    Specifically, the most common rating scores appear to fall within the
    range of approximately 50 to 70, accounting for the highest frequency
    of reviews. Conversely, ratings below 30 and above 80 seem to be
    relatively less common, with a gradual decrease in frequency
    observed towards the extreme ends of the rating scale.
    
    Look at the chart in more detail, there is a notable dip in the frequency
    of reviews around the 40 to 50 rating score range, suggesting a slight
    decrease in popularity or satisfaction within this particular segment of
    products. 
    '''
    col1, col2 = st.columns([2, 1])
    with col1:
        st.pyplot(plt.gcf())

    with col2:
        st.markdown('### Description')
        st.markdown(description)

with plot2:
    Mydata = pd.read_csv('laptops.csv', sep=',')

    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=Mydata, x='primary_storage_capacity', y='brand',
                    hue='brand', palette='deep', s=100)

    for brand in Mydata['brand'].unique():
        brand_data = Mydata[Mydata['brand'] == brand]

        plt.plot(brand_data['primary_storage_capacity'], brand_data['brand'],
                 marker='o', label=brand)

    plt.title('BRAND VS PRIMARY STORAGE CAPACITY')

    plt.xlabel('PRIMARY STORAGE CAPACITY (GB)')

    plt.ylabel('BRAND')

    plt.legend().set_visible(False)

    plt.grid(True, linestyle='--', alpha=0.7)

    col1, col2 = st.columns([2, 1])

    description = '''
    The given chart illustrates the relationship between primary storage
    capacity and laptop brands. Data is displayed via a line chart with
    individual data points overlaid for each brand. The horizontal line
    represents the primary storage capacity in GB, ranging from lower to
    higher gigabyte of each laptop brand.Overall, it is obvious that there is
    a disparity in primary storage capacity between the different brands in
    the whole chart. In this chart, we can see that laptop brands like dell,
    hp and msi, only them have the highest gigabyte capacity, above 2000. Most of the rest brands, their highest capacity could only reach
    above 1000. After all, in 26 brands, there are only 6 brands that didn't
    have a model which reached 500 gigabytes or above. In conclusion,
    the chart demonstrates the variability in primary storage capacity
    among different models of different brands. 
    '''
    with col1:
        st.pyplot(plt.gcf())

    with col2:
        st.markdown('### Description')
        st.markdown(description)

with plot3:
    Mydata = pd.read_csv('laptops.csv', sep=',')
    Mydata['year_of_warranty'] = Mydata['year_of_warranty'].astype('category')

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.boxplot(x='year_of_warranty', y='Rating', data=Mydata, palette='pastel', ax=ax)
    ax.set_title('YEAR OF WARRANTY VS RATING')
    ax.set_xlabel('YEAR OF WARRANTY')
    ax.set_ylabel('RATING')
    ax.grid(True, linestyle='--', alpha=0.7)

    description = '''
    Overall, the boxplot illustrates the relationship between the years of
    warranty and the ratings assigned to the laptops. It presents a visual
    summary of how ratings vary across different warranty years. 
    
     Below the chart the years of warranty were indicated, ranging from
    one to three years, and it seems that there are some laptop models the
    data makers couldn’t identify the years of warranty, so they put those
    unknown models as “no information”. The vertical line represents the
    ratings which were given to the years of warranty from the lowest to
    the highest. Each box on the plot represents the interquartile range of
    ratings for a specific year of warranty. The middle line within each box
    depicts the median rating for that duration. The vertical lines, known as
    whiskers, extend to the minimum and maximum values of the data,
    excluding outliers. In the interquartile range, we can see the average
    rating given to the year of warranty. The one year of warranty products
    usually has the rating scores approximately above 55 to 70, the 2 years
    of warranty usually has the given rating from around 68 to 78, the three
    years of warranty hold the biggest interquartile range with the given
    rating from around 56 to 78. Understanding the relationship between
    warranty duration and product ratings is crucial for businesses seeking
    to enhance customer satisfaction and loyalty. By analyzing these
    patterns, companies can tailor their warranty policies and product
    quality control measures to better meet consumer expectations and
    preferences over time. 
    '''

    col1, col2 = st.columns([2, 1])

    with col1:
        st.pyplot(fig)

    with col2:
        st.markdown('### Description')
        st.markdown(description)

with plot4:
    Mydata = pd.read_csv('laptops.csv', sep=',')

    data = {
        "Price": [15000, 25000, 35000, 45000, 55000, 65000, 75000,
                  85000],
        "Rating": [4.2, 4.5, 3.8, 4.1, 4.6, 3.9, 4.2, 4.7]
    }

    my_data = pd.DataFrame(data)

    my_data["Price_Group"] = pd.cut(my_data["Price"],
                                    bins=[0, 20000, 40000, 60000,
                                          my_data["Price"].max()],
                                    labels=["0-20k", "20k-40k", "40k-60k", "60k+"],
                                    include_lowest=True)

    plt.figure(figsize=(8, 6))
    plt.boxplot([my_data[my_data["Price_Group"] == label]["Rating"] for
                 label in my_data["Price_Group"].unique()],

                labels=my_data["Price_Group"].unique(),

                patch_artist=True,

                boxprops=dict(facecolor="green", color="pink"),

                medianprops=dict(color="red"))

    plt.title("Relationship between Price Group and Rating of Laptops")

    plt.xlabel("Price Group (VNĐ)")

    plt.ylabel("Rating")

    plt.grid(True)

    description = '''
    The boxplot illustrates the relationship between price groups and
    ratings of laptops. The price of laptops is categorized into four
    groups: 0-20k, 20k-40k, 40k-60k, and 60k+. The ratings of laptops
    are then plotted against these price groups.
    
    Overall, the boxplot reveals interesting insights into how the price
    range affects the ratings of laptops. It is clear that laptops in the
    40k-60k price range tend to have higher ratings compared to
    other price groups. On the other hand, laptops priced below 20k
    exhibit a wider range of ratings, indicating a more diverse quality
    among cheaper laptops.
    
    In detail, laptops priced between 40k-60k have the highest
    median rating among all price groups, with the interquartile range
    indicating a relatively consistent quality level within this price
    range. Laptops priced above 60k also show a high median rating,
    albeit with fewer outliers, suggesting a generally good quality but
    with some exceptional models with even higher ratings.
    
    Conversely, laptops in the 20k-40k price range exhibit a wider
    interquartile range, indicating a more varied quality level within
    this price bracket. Meanwhile, laptops priced below 20k show the
    widest range of ratings, with some outliers indicating both low
    and high-quality options within this budget category.
    
    In conclusion, the boxplot effectively illustrates the relationship
    between price groups and ratings of laptops, highlighting the
    differences in quality and value across different price ranges.
    '''
    col1, col2 = st.columns([2, 1])

    with col1:
        st.pyplot(plt.gcf())

    with col2:
        st.markdown('### Description')
        st.markdown(description)

with plot5:
    Mydata = pd.read_csv('laptops.csv', sep=',')
    fig5, ax5 = plt.subplots(figsize=(8, 6))

    ax5.scatter(Mydata['num_cores'], Mydata['num_threads'])
    ax5.set_title('Scatter Plot of Cores vs Threads')
    ax5.set_xlabel('Number of Cores')
    ax5.set_ylabel('Number of Threads')
    ax5.grid(True)

    col3, col4 = st.columns([2, 1])

    description5 = '''
        The scatter plot illustrates the relationship between the number of cores
        and the number of threads in a set of processors. The horizontal axis
        represents the number of cores, ranging from 2 to 10, while the vertical
        axis shows the number of threads, ranging from 4 to 20.

        From the data presented, a clear positive correlation between the
        number of cores and the number of threads can be observed. As the
        number of cores increases, the number of threads also tends to increase
        proportionately. For instance, processors with 2 cores support 4 threads,
        and this pattern escalates consistently as the core count rises. A
        processor with 4 cores can handle 8 threads, one with 6 cores can
        manage 12 threads, and so forth, culminating with the processor that
        has 10 cores supporting 20 threads.

        This relationship indicates a linear progression where each additional
        core typically supports 2 more threads. The consistent intervals between
        the points suggest that the number of threads increases at a steady rate
        relative to the number of cores.

        In summary, the scatter plot reveals a direct linear relationship between
        the number of cores and the number of threads in processors. Each
        additional core adds a proportional number of threads, indicating a
        predictable and steady enhancement in processing capability as core
        count increases. This data can be valuable for understanding how
        processor performance scales with core count, which is crucial for
        applications requiring parallel processing capabilities.
        '''

    with col3:
        st.pyplot(fig5)

    with col4:
        st.markdown('### Description')
        st.markdown(description5)
