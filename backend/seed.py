from app import app
from models import db, Product

products = [
    Product(
        name="DJI Mini 2 SE",
        type="drone",
        price="€349",
        description="Lightweight drone with 2.7K video and long flight time.",
        full_description="The DJI Mini 2 SE is a compact and ultra-light drone designed for beginners and travelers. It features 2.7K video recording, up to 31 minutes of flight time, strong wind resistance for its size, and intuitive controls. Its lightweight design allows it to bypass many regulatory restrictions, making it ideal for casual and everyday aerial photography.",
        image="https://s13emagst.akamaized.net/products/53306/53305567/images/res_f0df34e50fd345b71c537306d360eec4.jpg"
    ),
    Product(
        name="DJI Air 3",
        type="drone",
        price="€1099",
        description="Dual-camera drone with advanced obstacle sensing.",
        full_description="The DJI Air 3 features a dual-camera system with wide-angle and telephoto lenses, delivering stunning 4K video quality. It includes omnidirectional obstacle sensing, intelligent flight modes, and extended battery life. Designed for enthusiasts and semi-professionals, it balances portability with powerful imaging capabilities.",
        image="https://store.dji.bg/img/p/8/1/0/2/8102-large_default.jpg"
    ),
    Product(
        name="DJI Mavic 3 Classic",
        type="drone",
        price="€1499",
        description="Professional drone with Hasselblad camera.",
        full_description="The DJI Mavic 3 Classic is built for professional creators, featuring a Hasselblad camera capable of recording 5.1K video with exceptional color accuracy. It offers advanced safety features, long flight time, and precise controls, making it suitable for cinematic production and commercial work.",
        image="https://s13emagst.akamaized.net/products/50112/50111907/images/res_50f3bef294d609d6fc4143d39a6beb58.jpg"
    ),
    Product(
        name="Autel EVO Lite+",
        type="drone",
        price="€1299",
        description="6K drone with strong low-light performance.",
        full_description="The Autel EVO Lite+ is equipped with a powerful camera capable of shooting 6K video and featuring an adjustable aperture. It excels in low-light conditions and provides long flight time, intelligent flight modes, and robust obstacle avoidance, making it a strong alternative to DJI drones.",
        image="https://aerocam.bg/image/cache/catalog/AUTEL/Autel-LITE/autel-lite-plus-dron-nalichen-bulgaria-aerocam-900x900.jpg"
    ),
    Product(
        name="Parrot Anafi",
        type="drone",
        price="€599",
        description="Portable 4K HDR drone with unique gimbal.",
        full_description="The Parrot Anafi is a lightweight and ultra-portable drone featuring a 4K HDR camera with a unique 180-degree tilt gimbal. It is designed for creators who value mobility and flexibility, offering quiet operation, quick deployment, and solid image quality in a compact form factor.",
        image="https://www.parrot.com/assets/s3fs-public/styles/lg/public/2022-03/anafi-usa.jpg"
    ),
    Product(
        name="Skydio 2+",
        type="drone",
        price="€1,099",
        description="Autonomous drone with best-in-class avoidance.",
        full_description="The Skydio 2+ is an autonomous drone known for its industry-leading obstacle avoidance and AI-powered tracking. It is ideal for action sports and dynamic environments, allowing users to capture complex shots without manual control. The drone focuses on autonomy and safety rather than manual cinematography.",
        image="https://mfe-is.com/wp-content/uploads/2024/09/Skydio-2-Hero.png"
    ),
]

with app.app_context():
    db.session.add_all(products)
    db.session.commit()
