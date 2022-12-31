import React from 'react';
import { EditOutlined, EllipsisOutlined, ClockCircleOutlined } from '@ant-design/icons';
import { Col, Row, Carousel, Avatar, Card } from 'antd';
import slide1 from "../assets/img7.png";
import slide2 from "../assets/img2.jpg";
import slide3 from "../assets/img9.jpeg";
import slide4 from "../assets/img.jpg";

const { Meta } = Card;
const Home = () => {
  const settings = {
    dots: false,
  };
  return (
    <>
      <div className='container-home'>
        <Row>
          <Col span={12}>
            <div className='container-content'>
              <h1>A Guide For Entrepreneurs And New Employers In Global Companies</h1>
              <p>Passport To Business is a course that guides entrepreneurs and global companies on the fundamentals of business concepts.</p>
            </div>
          </Col>
          <Col span={12}>
            <Carousel autoplay className='container-slides' {...settings}>
              <div>
                <img className="imgslide" src={slide1} alt="one"/>
              </div>
              <div>
                <img className="imgslide" src={slide2} alt="two"/>
              </div>
              <div>
                <img className="imgslide" src={slide3} alt="three"/>
              </div>
              <div>
                <img className="imgslide" src={slide4} alt="four"/>
              </div>
            </Carousel>
          </Col>
        </Row> 
      </div>
      <div className='container-video'>
        <Row>
          <Col span={12}>
            <div>
              <iframe title="vimeo-player" src="https://player.vimeo.com/video/367019151" frameBorder="0" allowFullScreen></iframe>
            </div>
          </Col>
          <Col span={12}>
            <div className='container-content-video'>
              <h1>Passport To Business</h1>
              <p>Passport To Business is a Global Initiatives Inc. product developed for Kayana. It has curated practical courses for entrepreneurs who are starting their business to those businesses that are ready for the global market.</p>
            </div> 
          </Col>
        </Row>
      </div>
      <div className='container-courses'>
        <Card
          style={{
            width: 300,
          }}
          cover={
            <img
              alt="example"
              src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png"
            />
          }
          actions={[
            <ClockCircleOutlined key="duration" />,
            <EditOutlined key="edit" />,
            <EllipsisOutlined key="ellipsis" />,
          ]}
        >
        <Meta
          avatar={<Avatar src="https://joeschmoe.io/api/v1/random" />}
          title="Card title"
          description="This is the description"
        />
        </Card>
      </div>
        
    </>
  )
}

export default Home