import React, { useState } from "react";

const AlienSurvivalGuide = () => {
  const [articles, setArticles] = useState([
    {
      id: 1,
      title: "How to Prepare Your Dog for an Alien Invasion",
      points: [
        {
          title: "Mental preparation techniques for your dog",
          content:
            "Help your dog acclimate to unusual sights and sounds gradually, using positive reinforcement to associate these with safety and comfort.",
        },
        {
          title: "Physical conditioning exercises",
          content:
            "Regular walks and exercises that simulate sudden movements and loud noises can prepare your dog physically for unexpected events during an alien invasion.",
        },
        {
          title: "Early training and exposure to unusual stimuli",
          content:
            "Introduce your dog to environments and scenarios that mimic potential alien encounters early on, teaching them appropriate responses and behaviors.",
        },
      ],
    },
    {
      id: 2,
      title: "Survival Gear: Must-Haves for You and Your Dog",
      points: [
        {
          title: "Protective outerwear for humans and dogs",
          content:
            "Invest in durable, weather-resistant clothing and gear that provide both you and your dog protection from the elements and potential hazards.",
        },
        {
          title: "Communication devices",
          content:
            "Carry devices that allow for effective communication in case of separation or emergencies, ensuring you can stay in contact and coordinate with others.",
        },
        {
          title: "Specialized pet provisions",
          content:
            "Pack essential items such as food, water, medications, and comfort items specifically tailored to meet your dog's needs during prolonged periods away from home.",
        },
      ],
    },
    {
      id: 3,
      title: "Training Your Dog to Detect Alien Threats",
      points: [
        {
          title: "Structured training exercises",
          content:
            "Utilize systematic training methods that teach your dog to recognize and respond to unusual scents, sounds, and behaviors associated with potential alien threats.",
        },
        {
          title: "Behavioral conditioning techniques",
          content:
            "Reinforce desired behaviors through positive reinforcement, ensuring your dog remains attentive and responsive during training sessions focused on alien detection.",
        },
        {
          title: "Enhancing your dog's senses and awareness",
          content:
            "Engage in activities that stimulate your dog's senses and promote heightened awareness, enhancing their ability to detect and alert you to potential alien presence.",
        },
      ],
    },
  ]);

  const [selectedArticle, setSelectedArticle] = useState(null);

  const handleClick = (id) => {
    const article = articles.find((article) => article.id === id);
    setSelectedArticle(article);
  };

  return (
    <div className="alien-survival-guide">
      <h1>Alien Invasion Survival Guide with Your Dog</h1>
      <ul>
        {articles.map((article) => (
          <li key={article.id}>
            <button onClick={() => handleClick(article.id)}>
              {article.title}
            </button>
          </li>
        ))}
      </ul>
      {selectedArticle && (
        <div className="selected-article">
          <h2>{selectedArticle.title}</h2>
          <ul>
            {selectedArticle.points.map((point, index) => (
              <li key={index}>
                <h3>{point.title}</h3>
                <p>{point.content}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default AlienSurvivalGuide;
