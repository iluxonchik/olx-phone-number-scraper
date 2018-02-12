""" Test the navigation on an OLX listing page """

from olxscraper.olx_listings import OlxListings
import unittest

PRODUCTS_FILE_PATH_FMT = 'tests/resources/listings/listing_{}_p_{}.html'


class OLXListingActionsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_all_listings_from_a_page(self):
        """ test that all listing urls from a page are obtained """
        olx = OlxListings(url='file://tests/resources/listings/listing_1_p_1.html')

        expected_listing_urls = [
                                    'https://www.olx.pt/anuncio/iphone-6s-16gb-branco-desbloqueado-IDAYhGu.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6s-16gb-branco-desbloqueado-IDAYhGu.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-7-plus-IDATDfA.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-space-gray-64gb-IDAY6iU.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-prata-btanco-IDAY3ZC.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-galaxy-j1-excelente-estado-IDAY2sO.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/huawei-p9-lite-IDAXY4Y.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/honor-6x-como-novo-IDAXWiv.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-5c-como-novo-troco-por-samsung-s5-ou-s6-IDAMQxw.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-plus-vendo-ou-troco-IDAMhHL.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/wiko-sunset-2-IDAyYfP.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-j5-IDAXGZy.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-s7-edge-dourado-IDAXoPm.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-x-64gb-garantia-novo-selado-livre-de-operador-IDAXA35.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/lg-bello-IDAv3QD.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/telemvel-nokia-e71-como-novo-bloqueado-rede-vodafone-IDv3eav.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/qteck-s-100-novo-em-embalagem-original-IDv3eI6.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-64-gb-desbloquado-IDAXuZC.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/telemvel-desbloqueado-da-sharp-IDzosIx.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-s7-edge-IDAXt6n.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-galaxy-note-3-32-go-3-go-ram-bom-estado-IDATeu8.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-64gb-desbloqueado-IDAPfnD.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-se-16gb-IDAXlM2.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/telemoveis-diversas-marcas-carregadores-e-baterias-IDAXltQ.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-galaxy-s3-4g-IDAjSqf.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-7-32gb-preto-matte-capas-IDAXboZ.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/vendo-iphone-6-oferta-de-capas-IDAX4Wj.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/samsung-galaxy-j1-IDAS2le.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/huawei-p10-lite-preto-IDAVVVU.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/vendo-iphone-5s-pouco-usado-IDAVP2B.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-64gb-vodafone-IDAVKyo.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/telemvel-samsung-galaxy-fresh-IDASCba.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/huawei-y6-pro-2017-IDAVEUG.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/android-alcatel-pixi-3-IDAHyrm.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/android-aeg-ax350-IDAHyql.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/lg-p760-IDAGSAX.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-64gb-spacegrey-IDAV9Qr.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/componentes-samsung-galaxy-iii-neo-IDzPebF.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/iphone-6-plus-128gb-novo-garantia-2019-e-capa-dura-bateria-extra-IDABre2.html#ca62d95960',
                                    'https://www.olx.pt/anuncio/one-plus-x-IDAV7vh.html#ca62d95960'
                                ]
        obtained_listing_urls = olx.get_listing_urls_from_page()
        self.assertCountEqual(expected_listing_urls, obtained_listing_urls,
                              'Wrong listing urls parsed')

    def test_next_page_present_TRUE(self):
        olx = OlxListings(url='file://tests/resources/listings/listing_1_p_1.html')
        self.assertIsNotNone(olx.get_next_page_if_present(),
                              'Next page is present, but not marked as such')

    def test_next_page_present_FALSE(self):
        olx = OlxListings(url='file://tests/resources/listings/listing_1_p_2.html')
        self.assertIsNone(olx.get_next_page_if_present(),
                              'Next page is not present, but is marked as such')

    def test_all_listing_pages_are_read(self):
        pass
