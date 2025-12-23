from app import app
from models import db, Product

products = [
    Product(
        name="DJI Mini 2 SE",
        type="drone",
        price="€349",
        description="Lightweight drone with 2.7K video and long flight time.",
        full_description="The DJI Mini 2 SE is a compact and ultra-light drone designed for beginners and travelers. It features 2.7K video recording, up to 31 minutes of flight time, strong wind resistance for its size, and intuitive controls.",
        image="https://s13emagst.akamaized.net/products/53306/53305567/images/res_f0df34e50fd345b71c537306d360eec4.jpg"
    ),
    Product(
        name="DJI Air 3",
        type="drone",
        price="€1099",
        description="Dual-camera drone with advanced obstacle sensing.",
        full_description="The DJI Air 3 features a dual-camera system with wide-angle and telephoto lenses, omnidirectional obstacle sensing, and intelligent flight modes.",
        image="https://store.dji.bg/img/p/8/1/0/2/8102-large_default.jpg"
    ),
    Product(
        name="DJI Mavic 3 Classic",
        type="drone",
        price="€1499",
        description="Professional drone with Hasselblad camera.",
        full_description="The DJI Mavic 3 Classic is built for professional creators, featuring a Hasselblad camera capable of recording 5.1K video with exceptional color accuracy.",
        image="https://s13emagst.akamaized.net/products/50112/50111907/images/res_50f3bef294d609d6fc4143d39a6beb58.jpg"
    ),
    Product(
        name="Autel EVO Lite+",
        type="drone",
        price="€1299",
        description="6K drone with strong low-light performance.",
        full_description="The Autel EVO Lite+ offers a powerful 6K camera with adjustable aperture and excellent low-light performance.",
        image="https://aerocam.bg/image/cache/catalog/AUTEL/Autel-LITE/autel-lite-plus-dron-nalichen-bulgaria-aerocam-900x900.jpg"
    ),
    Product(
        name="Parrot Anafi",
        type="drone",
        price="€599",
        description="Portable 4K HDR drone with unique gimbal.",
        full_description="The Parrot Anafi is an ultra-portable drone with a 180-degree tilt gimbal and 4K HDR camera.",
        image="https://www.parrot.com/assets/s3fs-public/styles/lg/public/2022-03/anafi-usa.jpg"
    ),
    Product(
        name="Skydio 2+",
        type="drone",
        price="€1099",
        description="Autonomous drone with best-in-class avoidance.",
        full_description="The Skydio 2+ features industry-leading AI obstacle avoidance and autonomous tracking.",
        image="https://mfe-is.com/wp-content/uploads/2024/09/Skydio-2-Hero.png"
    ),
    Product(
        name="DJI Mini 3",
        type="drone",
        price="€469",
        description="Ultra-light drone with improved camera and battery.",
        full_description="The DJI Mini 3 offers longer flight time, improved camera quality, and ultra-light portability.",
        image="https://s13emagst.akamaized.net/products/50973/50972590/images/res_d0e042af3501796e7c29989f22d365ee.jpg"
    ),
    Product(
        name="DJI Mini 4 Pro",
        type="drone",
        price="€829",
        description="Advanced mini drone with obstacle avoidance.",
        full_description="The DJI Mini 4 Pro combines ultra-light design with omnidirectional obstacle sensing and advanced video features.",
        image="https://se-cdn.djiits.com/tpc/uploads/carousel/image/f96def8770cb7529d7a98731fa2117dd@ultra.jpg"
    ),
    Product(
        name="DJI Avata",
        type="drone",
        price="€1199",
        description="Immersive FPV drone for cinematic flying.",
        full_description="The DJI Avata is a compact FPV drone designed for immersive and safe close-range flying.",
        image="https://store.dji.bg/img/p/6/8/7/2/6872-large_default.jpg"
    ),
    Product(
        name="DJI FPV",
        type="drone",
        price="€999",
        description="High-speed FPV drone with cinematic control.",
        full_description="The DJI FPV offers high-speed performance with intuitive control and advanced safety features.",
        image="https://store.dji.bg/c/80-medium_default/dji-fpv-drones.jpg"
    ),
    Product(
        name="Autel EVO Nano+",
        type="drone",
        price="€649",
        description="Compact drone with excellent low-light camera.",
        full_description="The Autel EVO Nano+ features an RYYB sensor for outstanding low-light photography in a compact body.",
        image="https://drones.bg/wp-content/uploads/2023/06/dron-autel-evo-nano-plus.jpg"
    ),
    Product(
        name="Ryze Tello",
        type="drone",
        price="€119",
        description="Educational drone for beginners and kids.",
        full_description="The Ryze Tello is a beginner-friendly drone designed for learning, coding, and basic aerial photography.",
        image="https://m.media-amazon.com/images/I/615aqdHoR6L.jpg"
    ),
    Product(
        name="DJI Mini 2 Body Shell",
        type="accessory",
        price="€39",
        description="Replacement body shell for DJI Mini 2.",
        full_description="Original replacement body shell for DJI Mini 2 drones.",
        image="https://5.imimg.com/data5/SELLER/Default/2023/7/326210089/EY/AO/KH/22020579/hb96b7b22df194cdbb1da3f13ce4ee324d-jpg-640x640q90-500x500.jpg"
    ),
    Product(
        name="DJI Mavic Mini 3 Motor Arm",
        type="accessory",
        price="€29",
        description="Replacement motor arm for Mini 3.",
        full_description="Replacement motor arm for DJI Mavic Mini 3 drones.",
        image="https://img.fruugo.com/product/0/75/1628417750_0340_0340.jpg"
    ),
    Product(
        name="DJI Mavic 3 Pro",
        type="drone",
        price="€2199",
        description="Flagship triple-camera professional drone.",
        full_description="The DJI Mavic 3 Pro features a triple-camera system including Hasselblad and telephoto lenses for ultimate creative flexibility.",
        image="https://store.dji.bg/6082-thickbox_default/dji-mavic-3-pro-dji-rc.jpg"
    ),
    Product(
        name="DJI Inspire 3",
        type="drone",
        price="€16499",
        description="Cinema-grade drone for professional filmmaking.",
        full_description="The DJI Inspire 3 is a top-tier cinema drone designed for Hollywood-level productions with full-frame sensors.",
        image="https://magazin.photosynthesis.bg/206470-large_default/dron-dji-inspire-3.jpg"
    ),
    Product(
        name="Autel EVO II Pro V3",
        type="drone",
        price="€1899",
        description="6K professional drone with 1-inch sensor.",
        full_description="The Autel EVO II Pro V3 features a 6K camera with a 1-inch sensor for professional aerial imaging.",
        image="https://shop.autelrobotics.com/cdn/shop/files/10_c96a6466-0ef4-43d2-8dc4-7085d405d13c_1100x.jpg?v=1718206908"
    ),
    Product(
        name="DJI Neo",
        type="drone",
        price="€299",
        description="Ultra-compact beginner-friendly drone.",
        full_description="The DJI Neo is a compact and lightweight drone designed for beginners and casual users.",
        image="https://store.dji.bg/7259-large_default/dji-neo-no-rc.jpg"
    ),
    Product(
        name="DJI RC 2 Remote Controller",
        type="accessory",
        price="€369",
        description="Smart controller with built-in display.",
        full_description="The DJI RC 2 remote controller features a built-in high-bright display and advanced connectivity.",
        image="https://store.dji.bg/6326-large_default/dji-rc-2.jpg"
    ),
    Product(
        name="DJI Mini 3 Intelligent Flight Battery Plus",
        type="accessory",
        price="€89",
        description="Extended flight battery for DJI Mini 3.",
        full_description="High-capacity intelligent battery for extended flight time with DJI Mini 3.",
        image="https://store.dji.bg/4708-thickbox_default/dji-mini-3-pro-intelligent-flight-battery.jpg"
    ),
    Product(
        name="DJI Air 3 Propellers",
        type="accessory",
        price="€19",
        description="Original replacement propellers for Air 3.",
        full_description="Original DJI replacement propeller set designed specifically for the DJI Air 3.",
        image="https://se-cdn.djiits.com/tpc/uploads/photo/image/6df762004f2ec1b75169cba758ee24c3@large.jpg"
    ),
    Product(
        name="DJI FPV Goggles V2",
        type="accessory",
        price="€549",
        description="FPV goggles for immersive flight.",
        full_description="DJI FPV Goggles V2 provide a fully immersive flying experience with low-latency video.",
        image="https://store.dji.bg/6177-thickbox_default/dji-goggles-2.jpg"
    ),
    Product(
        name="DJI Mavic 3 Intelligent Flight Battery",
        type="accessory",
        price="€219",
        description="Spare battery for DJI Mavic 3 series.",
        full_description="High-capacity intelligent battery compatible with DJI Mavic 3 series drones.",
        image="https://store.dji.bg/4254-large_default/dji-mavic-3-intelligent-flight-battery.jpg"
    ),
]

with app.app_context():
    db.session.add_all(products)
    db.session.commit()
